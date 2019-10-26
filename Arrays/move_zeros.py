def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j] = nums[i]
            j += 1
    for i in range(j, len(nums)):
        nums[i] = 0

    return nums

def moveZerosApproach2(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            count += 1
        else:
            if count != 0:
                nums[i - count] = nums[i]
                nums[i] = 0

    return nums

nums = [0,1,0,3,12]
print(moveZeroes(nums))
print(moveZerosApproach2(nums))