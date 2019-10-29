'''
Select the smallest smallest from unsorted list and move it to sorted portion partition
'''

def selection_sort(nums):

    for i in range(len(nums)):
        min_index = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
                nums[i], nums[j] = nums[j], nums[i]

    return nums

nums = [2,5,1,6,8]
print(selection_sort(nums))