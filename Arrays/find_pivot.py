def find_pivot(nums):

    left = 0
    right = len(nums) - 1

    left_sum, right_sum = nums[left], nums[right]

    while left <= right:
        if left_sum == right_sum and left + 1 == right - 1:
            return left + 1
        elif left_sum < right_sum:
            left += 1
            left_sum += nums[left]
        else:
            right -= 1
            right_sum += nums[right]

    return -1

nums = [1, 7, 3, 6, 5, 6]
print(find_pivot(nums))

nums = [-2, 5, 6, 8, 2, 7]
print(find_pivot(nums))

nums = [1, 2, 3]
print(find_pivot(nums))