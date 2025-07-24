# bubble sort
def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        flag = False
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                flag = True
        if not flag: break



# Example
nums = [5, 2, 9, 1, 5, 6]
nums = [1,2,3,4,5,6]
bubble_sort(nums)
print("Sorted array:", nums)
