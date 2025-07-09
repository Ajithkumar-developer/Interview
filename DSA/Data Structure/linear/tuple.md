# Python Tuple Operations and Methods - Examples with Definitions

```python
# Initial tuple
t = (1, 2, 3, 2, 4)
print("Initial tuple:", t)  # (1, 2, 3, 2, 4)

# count(x): Returns number of times x appears in the tuple
print("t.count(2):", t.count(2))  # 2

# index(x): Returns the first index of value x
print("t.index(3):", t.index(3))  # 2

# len(): Returns the number of elements in the tuple
print("len(t):", len(t))  # 5

# Accessing elements by index
print("t[0]:", t[0])  # 1
print("t[-1]:", t[-1])  # 4

# Slicing
print("t[1:4]:", t[1:4])  # (2, 3, 2)

# Iteration
print("Iterating over tuple:")
for item in t:
    print(item, end=' ')  # 1 2 3 2 4
print()

# Membership test
print("Is 3 in t?", 3 in t)  # True

# Concatenation
t1 = (10, 11)
combined = t + t1
print("Concatenated tuple:", combined)  # (1, 2, 3, 2, 4, 10, 11)

# Repetition
print("Repetition:", t1 * 2)  # (10, 11, 10, 11)

# Nested tuples
nested = (1, (2, 3), 4)
print("Nested tuple:", nested)  # (1, (2, 3), 4)
print("Access nested element nested[1][1]:", nested[1][1])  # 3

# Tuples are immutable
# The following line would raise an error:
# t[0] = 100  # TypeError: 'tuple' object does not support item assignment

# Converting list to tuple
lst = [5, 6, 7]
tpl_from_list = tuple(lst)
print("Tuple from list:", tpl_from_list)  # (5, 6, 7)

# Tuple unpacking
a, b, c, d, e = t
print("Unpacked values:", a, b, c, d, e)  # 1 2 3 2 4
