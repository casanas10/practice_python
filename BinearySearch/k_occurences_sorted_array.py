'''
Find the total occurences of k in a sorted array

Examples :

Input: arr[] = {1, 1, 2, 2, 2, 2, 3,},   x = 2
Output: 4 // x (or 2) occurs 4 times in arr[]

Input: arr[] = {1, 1, 2, 2, 2, 2, 3,},   x = 3
Output: 1

Input: arr[] = {1, 1, 2, 2, 2, 2, 3,},   x = 1
Output: 2

Input: arr[] = {1, 1, 2, 2, 2, 2, 3,},   x = 4
Output: -1 // 4 doesn't occur in arr[]

'''


'''
Time Complexity : O(n) - linear scan  
Space Complexity: O(1)
'''
def k_occurences_linear_scan(nums, k):
    count = 0
    for i in range(len(nums)):
        if nums[i] == k:
            count += 1
    return count


def find_first(arr, low, high, k):

    if low > high:
        return -1

    mid = low + (high - low) // 2

    if (mid == 0 or arr[mid-1] < k) and arr[mid] == k:
        return mid
    elif arr[mid] < k:
        low = mid + 1
    else:
        high = mid - 1

    return find_first(arr, low, high, k)

def find_last(arr, low, high, k):
    if low > high:
        return -1

    mid = low + (high - low) // 2

    if (mid == len(arr) - 1 or arr[mid + 1] > k) and arr[mid] == k:
        return mid
    elif k < arr[mid]:
        high = mid - 1
    else:
        low = mid + 1

    return find_last(arr, low, high, k)


def k_occurences_using_two_bineary_search(nums, k):

    #get the index of the first occurences
    first_occur = find_first(nums, 0, len(nums)-1, k)

    #get the index of the last occurences
    last_occur = find_last(nums, 0, len(nums)-1, k)

    #return the difference + 1
    return last_occur - first_occur + 1




nums = [1,1,2,2,2,2,3]
k = 2
print(k_occurences_linear_scan(nums, k))
print(k_occurences_using_two_bineary_search(nums, k))