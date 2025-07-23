# Binary search

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            result = mid
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return result

numbers = [1, 3, 5, 7, 9, 11, 13]
target = 7
result = binary_search(numbers, target)

if result != -1:
    print(f"Found at index {result}")
else:
    print("Not found")
