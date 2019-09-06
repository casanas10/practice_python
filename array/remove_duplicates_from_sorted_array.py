'''
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.

'''

def remove_duplicates(nums):

    if len(nums) == 0: return 0

    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            nums[i+1] = nums[j]
            i += 1

    return i+1

def main():
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(remove_duplicates(nums))
if __name__ == "__main__":
    main()