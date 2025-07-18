# Prototype
The Prototype design pattern is used to create new objects by copying an existing object (called a prototype). 
This is especially useful when creating an object is expensive or complex, and you want to avoid recreating it from scratch.

### Pros:
- Avoids the cost of creating objects from scratch
- Easy to duplicate complex objects
- Hides the complexity of object construction
- Good for creating many similar objects (e.g., in games or editors)

### Cons:
- Cloning can be tricky with deeply nested or complex objects
- May require custom clone logic to handle internal state
- Harder to track changes if many copies exist

### Use When:
- Object creation is expensive (e.g., loading from a database or file)
- You need many similar objects with slight differences
- You want to keep construction logic out of the client

```python

# 1. define the prototype
# 2. create initial
# 3. clone and modify the prototype
import copy

# 1. define the prototype
class Robot:
    def __init__(self, name, robot_type, weapon):
        self.name = name
        self.robot_type = robot_type
        self.weapon = weapon

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Robot(Name : {self.name}, Type : {self.robot_type}, Weapon : {self.weapon})"

# 2. create initial
worker_robot = Robot("WorkerBot", "Worker", "Hammer")
print("\nOriginal Prototype Robot : ")
print(worker_robot)

# 3. clone and modify the prototype
robot1 = worker_robot.clone()
robot1.name = "WorkerBot-A"

robot2 = worker_robot.clone()
robot2.name = "WorkerBot-B"
robot2.weapon = "Wrench"

print("\nClonned Robots : ")
print(robot1)
print(robot2)

```
