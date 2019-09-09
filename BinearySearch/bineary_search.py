def bineary_search(nums, target):

    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # End Condition: left > right
    return -1

def main():

    nums = [-1,0,3,5,9,12]
    target = 9
    print(bineary_search(nums, target))

if __name__ == "__main__":
    main()