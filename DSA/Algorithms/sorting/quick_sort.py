# Quick sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)



nums = [9, 3, 7, 6, 2, 8]
sorted_nums = quick_sort(nums)
print("Sorted list:", sorted_nums)
