
def binary_search(nums, target):
    low, high = 0, len(nums)-1
    while low <= high:
        mid = low + (high - low) // 2
        mid_value = nums[mid]
        if mid_value == target:
            return mid
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def bineary_search_recursive(nums, target):
    def helper(nums, left, right, target):
        if left > right:
            return -1

        mid = left + (right - left) // 2  #to avoid overflow

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        return helper(nums, left, right, target)

    return helper(nums, 0, len(nums)-1, target)

def main():

    nums = [-1,0,3,5,9,12]
    target = 9
    print(binary_search(nums, target))

    print(bineary_search_recursive(nums, target))

if __name__ == "__main__":
    main()