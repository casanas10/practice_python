def search(nums, target):

    '''
    Use Bineary Search to find the pivot elements
    '''
    def find_rotate_index(left, right):
        if nums[left] < nums[right]:
            return 0

        while left <= right:
            pivot = (left + right) // 2
            if nums[pivot] > nums[pivot + 1]:
                return pivot + 1
            else:
                if nums[pivot] < nums[left]:
                    right = pivot - 1
                else:
                    left = pivot + 1

    def search(left, right):
        """
        Binary search
        """
        while left <= right:
            pivot = (left + right) // 2
            if nums[pivot] == target:
                return pivot
            else:
                if target < nums[pivot]:
                    right = pivot - 1
                else:
                    left = pivot + 1
        return -1

    n = len(nums)

    if n == 0:
        return -1
    if n == 1:
        return 0 if nums[0] == target else -1

    rotate_index = find_rotate_index(0, n - 1)

    # if target is the smallest element
    if nums[rotate_index] == target:
        return rotate_index
    # if array is not rotated, search in the entire array
    if rotate_index == 0:
        return search(0, n - 1)
    if target < nums[0]:
        # search on the right side
        return search(rotate_index, n - 1)
    # search on the left side
    return search(0, rotate_index)


def approach2(nums, target):

    left, right = 0, len(nums) - 1
    while left <= right:

        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        #if mid element is bigger than leftmost elem
        elif nums[mid] >= nums[left]:
            if target < nums[mid] and target >= nums[left]:
                right = mid - 1
            else:
                left = mid + 1
        # nums mid is smaller than first element which means not rotated
        else:
            if target > nums[mid] and target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


def main():

    nums = [4,5,6,7,0,1,2]
    target = 4

    print(approach2(nums, target))

if __name__ == "__main__":
    main()