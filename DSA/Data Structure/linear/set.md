# Python Set Operations and Methods - Examples with Definitions

```python
# Initial set
s = {1, 2, 3, 4}
print("Initial set:", s)  # {1, 2, 3, 4}

# add(x): Adds an element to the set
s.add(5)
print("After add(5):", s)  # {1, 2, 3, 4, 5}

# update(iterable): Adds multiple elements
s.update([6, 7])
print("After update([6, 7]):", s)  # {1, 2, 3, 4, 5, 6, 7}

# remove(x): Removes x, raises KeyError if not found
s.remove(7)
print("After remove(7):", s)  # {1, 2, 3, 4, 5, 6}

# discard(x): Removes x if present, does nothing if not
s.discard(10)
print("After discard(10):", s)  # No error, set unchanged

# pop(): Removes and returns an arbitrary element
popped = s.pop()
print("After pop():", s)
print("Popped element:", popped)

# clear(): Removes all elements
temp_set = s.copy()
temp_set.clear()
print("After clear():", temp_set)  # set()

# copy(): Returns a shallow copy
copied = s.copy()
print("Copied set:", copied)

# Set union: Combines elements from both sets
a = {1, 2, 3}
b = {3, 4, 5}
print("a | b:", a | b)  # {1, 2, 3, 4, 5}
print("a.union(b):", a.union(b))  # {1, 2, 3, 4, 5}

# Set intersection: Common elements
print("a & b:", a & b)  # {3}
print("a.intersection(b):", a.intersection(b))  # {3}

# Set difference: Elements in a not in b
print("a - b:", a - b)  # {1, 2}
print("a.difference(b):", a.difference(b))  # {1, 2}

# Set symmetric difference: Elements in either set but not both
print("a ^ b:", a ^ b)  # {1, 2, 4, 5}
print("a.symmetric_difference(b):", a.symmetric_difference(b))  # {1, 2, 4, 5}

# issubset(): Checks if a is subset of b
print("a.issubset(b):", a.issubset(b))  # False

# issuperset(): Checks if a is superset of b
print("a.issuperset(b):", a.issuperset(b))  # False

# isdisjoint(): Checks if two sets have no elements in common
print("a.isdisjoint({6, 7}):", a.isdisjoint({6, 7}))  # True

# Set comprehension
squared = {x**2 for x in range(1, 6)}
print("Set comprehension:", squared)  # {1, 4, 9, 16, 25}
