# ZOHO --> Taxi Booking Interview question

#  Design a Call taxi booking application
# -There are n number of taxi’s. For simplicity, assume 4. But it should work for any number of taxi’s.
# -The are 6 points(A,B,C,D,E,F)
# -All the points are in a straight line, and each point is 15kms away from the adjacent points.
# -It takes 60 mins to travel from one point to another
# -Each taxi charges Rs.100 minimum for the first 5 kilometers and Rs.10 for the subsequent kilometers.
# -For simplicity, time can be entered as absolute time. Eg: 9hrs, 15hrs etc.
# -All taxi’s are initially stationed at A.
# -When a customer books a Taxi, a free taxi at that point is allocated
# -If no free taxi is available at that point, a free taxi at the nearest point is allocated.
# -If two taxi’s are free at the same point, one with lower earning is allocated
# -Note that the taxi only charges the customer from the pickup point to the drop point. Not the distance it travels from an adjacent point to pickup the customer.
# -If no taxi is free at that time, booking is rejected


POINTS = ['A', 'B', 'C', 'D', 'E', 'F']
DISTANCE_BETWEEN_POINTS = 15  # in km
TIME_BETWEEN_DISTANCE = 1     # 1 hour between adjacent points

def get_point_index(point):
    return POINTS.index(point)

def calculate_distance(p1, p2):
    return abs(get_point_index(p1) - get_point_index(p2)) * DISTANCE_BETWEEN_POINTS

def calculate_travel_time(p1, p2):
    return abs(get_point_index(p1) - get_point_index(p2)) * TIME_BETWEEN_DISTANCE


class Taxi:
    def __init__(self, taxi_id):
        self.taxi_id = taxi_id
        self.current_location = 'A'
        self.free_at = 0  # in hours
        self.total_earnings = 0
        self.trips = []

    def is_available(self, pickup_point, pickup_time):
        time_to_reach = calculate_travel_time(self.current_location, pickup_point)
        # Taxi must be free early enough to travel to pickup
        return self.free_at + time_to_reach <= pickup_time

    def assign_trip(self, booking):
        distance = calculate_distance(booking.pickup, booking.drop)
        fare = 100 if distance <= 5 else 100 + (distance - 5) * 10

        self.current_location = booking.drop
        self.total_earnings += fare
        self.free_at = booking.pickup_time + calculate_travel_time(booking.pickup, booking.drop)
        self.trips.append((booking, fare))
        return fare


class Booking:
    def __init__(self, customer_id, pickup, drop, pickup_time):
        self.customer_id = customer_id
        self.pickup = pickup
        self.drop = drop
        self.pickup_time = pickup_time
        self.taxi_assigned = None
        self.fare = 0


class BookingManager:
    def __init__(self, number_of_taxis):
        self.taxis = [Taxi(i+1) for i in range(number_of_taxis)]

    def book_taxi(self, customer_id, pickup, drop, pickup_time):
        available_taxis = []

        for taxi in self.taxis:
            if taxi.is_available(pickup, pickup_time):
                distance_to_pickup = calculate_distance(taxi.current_location, pickup)
                available_taxis.append((taxi, distance_to_pickup))

        if not available_taxis:
            print(f"Booking Rejected for Customer-{customer_id}")
            return

        # Sort by distance to pickup, then by total earnings
        available_taxis.sort(key=lambda x: (x[1], x[0].total_earnings))

        chosen_taxi = available_taxis[0][0]
        booking = Booking(customer_id, pickup, drop, pickup_time)
        booking.taxi_assigned = chosen_taxi.taxi_id
        booking.fare = chosen_taxi.assign_trip(booking)

        print(f"Taxi-{chosen_taxi.taxi_id} booked for Customer-{customer_id} | Fare: Rs.{booking.fare}")

    def print_summary(self):
        print("\n--- Taxi Summary ---")
        for taxi in self.taxis:
            print(f"Taxi-{taxi.taxi_id} | Total Earnings: Rs.{taxi.total_earnings}")
            for trip, fare in taxi.trips:
                print(f"  -> Customer-{trip.customer_id} | {trip.pickup} to {trip.drop} at {trip.pickup_time}h | Fare: Rs.{fare}")
            print()


# Example usage
if __name__ == "__main__":
    manager = BookingManager(4)

    # Test bookings
    manager.book_taxi(customer_id=1, pickup='A', drop='D', pickup_time=9)
    manager.book_taxi(customer_id=2, pickup='B', drop='C', pickup_time=10)
    manager.book_taxi(customer_id=3, pickup='A', drop='F', pickup_time=10)
    manager.book_taxi(customer_id=4, pickup='A', drop='B', pickup_time=9)
    manager.book_taxi(customer_id=5, pickup='A', drop='F', pickup_time=10)  # May be rejected

    manager.print_summary()
