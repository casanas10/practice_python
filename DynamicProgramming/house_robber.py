def rob(nums):
    prevMax = 0
    currMax = 0

    for i in nums:
        temp = currMax
        currMax = max(prevMax + i, currMax)
        prevMax = temp

    return currMax

nums = [1,2,3,1]
print(rob(nums))