# Python List Operations and Methods - Examples with Definitions

```python
# Initial list
lst = [1, 2, 3]
print("Initial list:", lst)  # [1, 2, 3]

# append(x): Adds an item to the end of the list.
lst.append(4)
print("After append(4):", lst)  # [1, 2, 3, 4]

# extend(iterable): Adds all items from another iterable.
lst.extend([5, 6])
print("After extend([5, 6]):", lst)  # [1, 2, 3, 4, 5, 6]

# insert(i, x): Inserts item x at index i.
lst.insert(2, 'a')
print("After insert(2, 'a'):", lst)  # [1, 2, 'a', 3, 4, 5, 6]

# remove(x): Removes the first occurrence of x.
lst.remove('a')
print("After remove('a'):", lst)  # [1, 2, 3, 4, 5, 6]

# pop([i]): Removes and returns item at index i (last item if i is not specified).
popped = lst.pop(3)
print("After pop(3):", lst)  # [1, 2, 3, 5, 6]
print("Popped element:", popped)  # 4

# index(x): Returns the first index of value x.
index = lst.index(3)
print("Index of 3:", index)  # 2

# count(x): Returns the number of times x appears in the list.
count = lst.count(2)
print("Count of 2:", count)  # 1

# sort(): Sorts the list in ascending order.
unsorted_lst = [3, 1, 4, 2]
unsorted_lst.sort()
print("Sorted list:", unsorted_lst)  # [1, 2, 3, 4]

# reverse(): Reverses the list in-place.
unsorted_lst.reverse()
print("Reversed list:", unsorted_lst)  # [4, 3, 2, 1]

# copy(): Returns a shallow copy of the list.
copied_lst = lst.copy()
print("Copied list:", copied_lst)  # [1, 2, 3, 5, 6]

# clear(): Removes all items from the list.
copied_lst.clear()
print("Cleared copied list:", copied_lst)  # []

# Slicing: Returns a sublist using indices.
sliced = lst[1:4]
print("Sliced lst[1:4]:", sliced)  # [2, 3, 5]

# Concatenation: Combines two lists using +
lst1 = [1, 2]
lst2 = [3, 4]
combined = lst1 + lst2
print("Concatenated list:", combined)  # [1, 2, 3, 4]

# Repetition: Repeats a list using *
repeated = lst1 * 2
print("Repeated list:", repeated)  # [1, 2, 1, 2]

# Membership: Checks if an item exists in the list.
print("Is 2 in lst?", 2 in lst)  # True

# len(): Returns the number of items in the list.
print("Length of lst:", len(lst))  # 5

# Iteration: Loop through items in the list.
print("Iterating through lst:")
for item in lst:
    print(item, end=' ')  # 1 2 3 5 6
print()

# List Comprehension: Create new list using an expression.
doubled = [x * 2 for x in lst]
print("List comprehension [x*2 for x in lst]:", doubled)  # [2, 4, 6, 10, 12]

# Nested List: A list inside another list.
nested = [1, [10, 20], 3]
print("Nested list:", nested)  # [1, [10, 20], 3]
print("Access nested element nested[1][0]:", nested[1][0])  # 10
