def dominantIndex(nums):

    if len(nums) < 2: return 0

    # find max
    max = float("-inf")
    maxIndex = 0
    for i, x in enumerate(nums):
        if x > max:
            max = x
            maxIndex = i

    # scan for 2x bigger elem than max
    second_max = float("-inf")
    for i, x in enumerate(nums):
        if max != x and x > second_max:
            second_max = x

    if max >= 2 * second_max:
        return maxIndex

    return -1

def dominantIndexApproach2(nums):
    m = max(nums)
    for x in nums:
        if x != m and m < 2 * x:
            return -1
    return nums.index(m)

nums = [3, 6, 1, 13, 0]
print(dominantIndex(nums))
print(dominantIndexApproach2(nums))


nums = [1,2,3,4]
print(dominantIndex(nums))
print(dominantIndexApproach2(nums))