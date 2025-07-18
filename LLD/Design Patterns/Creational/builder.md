# Builder
Separates the construction of a complex object from its representation, allowing the same building steps to create different types of objects.

### Pros
- Builds complex objects step-by-step
- Supports different representations with the same construction process
- Improves code clarity and flexibility
- Encapsulates object creation

### Cons
- More code and classes to maintain
- Can be overkill for simple objects
- Director and builder interfaces add extra complexity

```python
# 1. Define the product
# 2. Define the builder
# 3. client code

# 1. Define the product
class Computer:
    def __init__(self):
        self.processor = None
        self.ram = None
        self.storage = None
        self.graphics_card = None

    def __str__(self):
        return (
            f"Processor : {self.processor}\n"
            f"Ram : {self.ram}\n"
            f"Storage : {self.storage}\n"
            f"Graphics Card : {self.graphics_card}\n"
        )

# 2. Define the builder
class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def set_processor(self, processor):
        self.computer.processor = processor
        return self

    def set_ram(self, ram):
        self.computer.ram = ram
        return self

    def set_storage(self, storage):
        self.computer.storage = storage
        return self

    def set_graphics_card(self, graphics):
        self.computer.graphics_card = graphics
        return self

    def build(self):
        return self.computer


# 3. client code

gaming_computer = (
    ComputerBuilder()
    .set_processor("Intel i9")
    .set_ram("32GB")
    .set_storage("2TB SSD").set_graphics_card("NVIDIA RTX 4090")
    .build()
)

office_computer = (
    ComputerBuilder()
    .set_processor("Intel i5")
    .set_ram("16GB")
    .set_storage("1TB SSD")
    .set_graphics_card("Integrated Graphics")
    .build()
)

print("\nGaming Computer: ")
print(gaming_computer)
print("\nOffice Computer : ")
print(office_computer)

# Optional: Adding a Director
# A Director is optional but useful if you have predefined steps for creating certain types of objects.

class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct_gaming_computer(self):
        return (
            self.builder.set_processor("Intel i9")
            .set_ram("32GB")
            .set_storage("2TB SSD")
            .set_graphics_card("NVIDIA RTX 4090")
            .build()
        )

    def construct_office_computer(self):
        return (
            self.builder.set_processor("Intel i5")
            .set_ram("16GB")
            .set_storage("512GB SSD")
            .set_graphics_card("Integrated Graphics")
            .build()
        )

# Using the Director
# Create a builder
builder = ComputerBuilder()
director = Director(builder)

# Let the director handle the building process
gaming_computer = director.construct_gaming_computer()
print("Gaming Computer:")
print(gaming_computer)

office_computer = director.construct_office_computer()
print("\nOffice Computer:")
print(office_computer)

```
