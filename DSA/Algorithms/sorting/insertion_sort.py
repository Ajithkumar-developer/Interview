# Insertion sort (useful for linked list)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1

        while j >=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = key
    return arr


nums = [9, 5, 1, 4, 3]
sorted_nums = insertion_sort(nums)
print("Sorted list:", sorted_nums)
