# Designing a Parking Lot System

# Requirements
# The parking lot should have multiple levels, each level with a certain number of parking spots.
# The parking lot should support different types of vehicles, such as cars, motorcycles, and trucks.
# Each parking spot should be able to accommodate a specific type of vehicle.
# The system should assign a parking spot to a vehicle upon entry and release it when the vehicle exits.
# The system should track the availability of parking spots and provide real-time information to customers.
# The system should handle multiple entry and exit points and support concurrent access.


from enum import Enum
from threading import Lock
import logging
import uuid
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Vehicle and Parking Spot Types
class VehicleType(Enum):
    MOTORCYCLE = "Motorcycle"
    CAR = "Car"
    TRUCK = "Truck"

class ParkingSpotType(Enum):
    MOTORCYCLE = "Motorcycle"
    CAR = "Car"
    TRUCK = "Truck"

# Which vehicles can fit in which spots
SPOT_FIT_MAP = {
    VehicleType.MOTORCYCLE: [ParkingSpotType.MOTORCYCLE, ParkingSpotType.CAR, ParkingSpotType.TRUCK],
    VehicleType.CAR: [ParkingSpotType.CAR, ParkingSpotType.TRUCK],
    VehicleType.TRUCK: [ParkingSpotType.TRUCK]
}

# Vehicle class
class Vehicle:
    def __init__(self, number_plate: str, vehicle_type: VehicleType):
        self.number_plate = number_plate
        self.vehicle_type = vehicle_type

# Ticket class
class Ticket:
    def __init__(self, vehicle: Vehicle, level_id: int, spot_id: str):
        self.ticket_id = str(uuid.uuid4())
        self.vehicle = vehicle
        self.level_id = level_id
        self.spot_id = spot_id
        self.entry_time = datetime.now()

# Parking Spot
class ParkingSpot:
    def __init__(self, spot_id: str, spot_type: ParkingSpotType):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.is_occupied = False
        self.vehicle = None

    def can_fit_vehicle(self, vehicle: Vehicle):
        return self.spot_type in SPOT_FIT_MAP[vehicle.vehicle_type] and not self.is_occupied

    def assign_vehicle(self, vehicle: Vehicle):
        self.vehicle = vehicle
        self.is_occupied = True

    def remove_vehicle(self):
        self.vehicle = None
        self.is_occupied = False

# Level containing multiple spots
class Level:
    def __init__(self, level_id: int, spots_per_type: dict):
        self.level_id = level_id
        self.spots = []
        self.lock = Lock()
        self.create_spots(spots_per_type)

    def create_spots(self, spots_per_type):
        for spot_type, count in spots_per_type.items():
            for i in range(count):
                spot_id = f"L{self.level_id}-{spot_type.name[0]}{i}"
                self.spots.append(ParkingSpot(spot_id, spot_type))

    def park_vehicle(self, vehicle: Vehicle):
        with self.lock:
            for spot in self.spots:
                if spot.can_fit_vehicle(vehicle):
                    spot.assign_vehicle(vehicle)
                    return spot
        return None

    def release_vehicle(self, number_plate: str):
        with self.lock:
            for spot in self.spots:
                if spot.is_occupied and spot.vehicle.number_plate == number_plate:
                    spot.remove_vehicle()
                    return spot
        return None

# Parking Lot class
class ParkingLot:
    def __init__(self, num_levels: int, spots_per_level: dict):
        self.levels = [Level(i, spots_per_level) for i in range(num_levels)]
        self.vehicle_registry = {}  # number_plate -> Ticket

    def park_vehicle(self, vehicle: Vehicle):
        if vehicle.number_plate in self.vehicle_registry:
            logging.warning(f"Vehicle {vehicle.number_plate} is already parked.")
            return None, None

        for level in self.levels:
            spot = level.park_vehicle(vehicle)
            if spot:
                ticket = Ticket(vehicle, level.level_id, spot.spot_id)
                self.vehicle_registry[vehicle.number_plate] = ticket
                logging.info(f"Vehicle {vehicle.number_plate} parked at {spot.spot_id} on level {level.level_id}")
                return ticket.ticket_id, spot.spot_id

        logging.warning(f"No available spot for vehicle: {vehicle.number_plate}")
        return None, None

    def exit_vehicle(self, number_plate: str):
        ticket = self.vehicle_registry.get(number_plate)
        if not ticket:
            logging.warning(f"Vehicle {number_plate} not found in registry.")
            return False

        level = self.levels[ticket.level_id]
        released_spot = level.release_vehicle(number_plate)
        if released_spot:
            duration = datetime.now() - ticket.entry_time
            fee = self.calculate_fee(duration)
            del self.vehicle_registry[number_plate]
            logging.info(f"Vehicle {number_plate} exited from {released_spot.spot_id} after {duration}. Fee: ${fee:.2f}")
            return True
        else:
            logging.warning(f"Vehicle {number_plate} was not found in level {ticket.level_id}.")
            return False

    def available_spots_info(self):
        info = {}
        for level in self.levels:
            for spot in level.spots:
                key = (level.level_id, spot.spot_type.name)
                if key not in info:
                    info[key] = 0
                if not spot.is_occupied:
                    info[key] += 1
        return info

    @staticmethod
    def calculate_fee(duration):
        # Example: $1 per hour
        hours = duration.total_seconds() / 3600
        return max(1.0, round(hours * 1.0, 2))  # At least $1

# Example usage
if __name__ == "__main__":
    spots_config = {
        ParkingSpotType.MOTORCYCLE: 2,
        ParkingSpotType.CAR: 3,
        ParkingSpotType.TRUCK: 1
    }

    parking_lot = ParkingLot(3, spots_config)

    v1 = Vehicle("ABC123", VehicleType.MOTORCYCLE)
    v2 = Vehicle("QWE234", VehicleType.CAR)
    v3 = Vehicle("XYZ987", VehicleType.TRUCK)

    parking_lot.park_vehicle(v1)
    parking_lot.park_vehicle(v2)
    parking_lot.park_vehicle(v3)

    logging.info("Available spots after parking:")
    logging.info(parking_lot.available_spots_info())

    parking_lot.exit_vehicle("ABC123")

    logging.info("Available spots after exit:")
    logging.info(parking_lot.available_spots_info())
