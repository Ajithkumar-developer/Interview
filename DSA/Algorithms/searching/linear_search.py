# linear search

def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index  # Found the target
    return -1  # Not found

numbers = [5, 3, 7, 1, 9, 2]
target = 9

result = linear_search(numbers, target)
print(f"Found at index: {result}" if result != -1 else "Not found")
