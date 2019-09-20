def merge_sort(nums):

    if len(nums) == 1: return

    midpoint = len(nums) // 2
    left = nums[:midpoint]
    right = nums[midpoint:]
    merge_sort(left)   #recursevely call the left side
    merge_sort(right)  #recursevely call the right side
    merge(left, right, nums)

    return nums

def merge(left, right, nums):

    i = 0
    j = 0
    k = 0

    #merge the elements of both arrays in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1

        k += 1

    #checking if there is any element remaining in either array
    while i < len(left):
        nums[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        nums[k] = right[j]
        j += 1
        k += 1

def main():
    nums = [5,1,4,2,8]
    print(merge_sort(nums))


if __name__ == "__main__":
    main()