def bubble_sort(nums):

    #let's use a flag that tells us when the array is sorted
    isSorted = False

    #keep looping until the array is sorted
    while not isSorted:

        #lets assume the array is sorted to begin with
        isSorted = True

        #walk through the array checking neighboring elements
        for i in range(len(nums) - 1):

            #if element to the right is bigger than elem on left, swap them
            if nums[i] > nums[i+1]:
                temp = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = temp

                #set the flag to False because is not sorted
                isSorted = False

    return nums

def countSwaps(nums):
    isSorted = False
    swaps = 0
    while not isSorted:
        isSorted = True
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                temp = nums[i]
                nums[i] = nums[i + 1]
                nums[i + 1] = temp
                swaps += 1
                isSorted = False

    return swaps

def main():
    nums = [5,1,4,2,8]
    print(bubble_sort(nums))

    nums = [4,2,3,1]
    print(countSwaps(nums))


if __name__ == "__main__":
    main()