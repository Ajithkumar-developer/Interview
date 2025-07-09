# Python Dictionary Operations and Methods - Examples with Definitions

```python
# Initial dictionary
d = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print("Initial dictionary:", d)
# {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Accessing value by key
print("d['name']:", d['name'])  # Alice

# get(key): Returns value for key, or None if not found
print("d.get('age'):", d.get('age'))  # 30
print("d.get('gender'):", d.get('gender'))  # None

# keys(): Returns a view of all keys
print("d.keys():", d.keys())  # dict_keys(['name', 'age', 'city'])

# values(): Returns a view of all values
print("d.values():", d.values())  # dict_values(['Alice', 30, 'New York'])

# items(): Returns view of (key, value) pairs
print("d.items():", d.items())
# dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])

# update(): Updates dictionary with another dictionary or key-value pairs
d.update({'age': 31, 'gender': 'Female'})
print("After update:", d)
# {'name': 'Alice', 'age': 31, 'city': 'New York', 'gender': 'Female'}

# pop(key): Removes specified key and returns the value
age = d.pop('age')
print("After pop('age'):", d)  # {'name': 'Alice', 'city': 'New York', 'gender': 'Female'}
print("Popped value:", age)  # 31

# popitem(): Removes and returns the last inserted key-value pair
last = d.popitem()
print("After popitem():", d)  # {'name': 'Alice', 'city': 'New York'}
print("Popped item:", last)  # ('gender', 'Female')

# setdefault(key, default): Returns value of key; sets it if not present
value = d.setdefault('country', 'USA')
print("After setdefault('country', 'USA'):", d)
# {'name': 'Alice', 'city': 'New York', 'country': 'USA'}
print("Returned value:", value)  # USA

# del: Removes item by key
del d['city']
print("After del d['city']:", d)  # {'name': 'Alice', 'country': 'USA'}

# clear(): Removes all items
d.clear()
print("After clear():", d)  # {}

# Dictionary creation using dict()
new_dict = dict(a=1, b=2)
print("Created with dict():", new_dict)  # {'a': 1, 'b': 2}

# Dictionary from list of tuples
tuple_dict = dict([('x', 10), ('y', 20)])
print("From list of tuples:", tuple_dict)  # {'x': 10, 'y': 20}

# Dictionary comprehension
squared = {x: x**2 for x in range(1, 4)}
print("Dict comprehension:", squared)  # {1: 1, 2: 4, 3: 9}

# Checking key existence
print("'a' in new_dict:", 'a' in new_dict)  # True

# Iterating over keys and values
print("Iterating over items:")
for key, value in new_dict.items():
    print(f"{key}: {value}")
# a: 1
# b: 2
