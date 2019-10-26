'''
Problem: Rotate an array of n elements to the right by k steps.  For example, with n = 7 and k = 3, the array
[1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4]. How many different ways do you know to solve this problem?

'''

'''
Simple approach 
-  create a new array and then copy elements to the new array. Then change the original array
Leads to 
Time Complexity O(n)
Space Complexity of O(n) because we create a new array
'''
def rotate_approach1(arr, k):
    new_array = [0] * len(arr)

    for i in range(k):
        new_array[i] = arr[len(arr)-k+i]

    i = 0
    for j in range(k, len(arr)):
        new_array[j] = arr[i]
        i+=1

    return new_array



'''
Better approach 
1. Divide the array two parts: 1,2,3,4 and 5, 6 
2. Rotate first part: 4,3,2,1,5,6 
3. Rotate second part: 4,3,2,1,6,5 
4. Rotate the whole array: 5,6,1,2,3,4

O(n) Time
O(1) Space
'''
def rotate(arr, k):

    def reverse(arr, left, right):
        if arr == None or len(arr) == 1:
            return

        while (left < right):
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    k = k % len(arr)

    if arr == None or k < 0:
        return -1

    a = len(arr) - k

    reverse(arr, 0, a-1)
    reverse(arr, a, len(arr) - 1)
    reverse(arr, 0, len(arr) - 1)

    return arr

arr = [1,2,3,4,5,6,7]
print(rotate(arr, 3))


arr = [1,2,3,4,5,6,7]
print(rotate_approach1(arr, 3))