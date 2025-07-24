# Merge sort
def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    mid = n // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    sorted = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted.append(left[i])
            i += 1
        else:
            sorted.append(right[j])
            j += 1
    sorted.extend(left[i:])
    sorted.extend(right[j:])

    return sorted


nums = [38, 27, 43, 3, 9, 82, 10]
sorted_nums = merge_sort(nums)
print("Sorted list:", sorted_nums)
