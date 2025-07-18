# Factory Method
The Factory Method defines an interface for creating an object, but lets subclasses alter the type of objects that will be created.
### Pros
- Decouples object creation from usage.
- Promotes consistency in object creation.
- Encourages Single Responsibility Principle (each class handles one concern).
### Cons
- Adds more classes and complexity.
- Might be overkill for simple object creation logic.


```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof! Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow! Meow!"

class Cow(Animal):
    def speak(self):
        return "Maa! Maa!"


class AnimalFactory:

    animal_map = {
        "dog": Dog(),
        "cat": Cat(),
        "cow": Cow()
    }

    @staticmethod
    def create_animal(animal_type):
        if animal_type in AnimalFactory.animal_map:
            return AnimalFactory.animal_map[animal_type]
        else:
            raise ValueError("Unknown Animal type")


animal = AnimalFactory.create_animal("dog")
print(animal.speak())

animal = AnimalFactory.create_animal("cat")
print(animal.speak())

animal = AnimalFactory.create_animal("cow")
print(animal.speak())
```
