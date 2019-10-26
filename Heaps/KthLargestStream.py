import heapq


'''
We can build a MinHeap that contains only k largest elements.
On add:

compare a new element x with min to decide if we should pop min and insert x
take into account a case when heap_size is less than k
Construction is simply calling the add function N times.

Time complexity:

Construction: O(N * logK)
Adding: O(logK)
Additional memory:
O(K) (can be reduced to O(1) by reusing memory of the existing array)
'''
class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)  #build min heap
        #pop elements until get to k size
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

    def add(self, val):
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        elif val > self.nums[0]:
            heapq.heapreplace(self.nums, val)

        return self.nums[0]  #nums[0] always has the kth largest element


'''
Approach 2 Using Binary Search to insert values and python sort to keep initially sort elements
'''
import bisect
class KthLargest_Approach2(object):

    def __init__(self, k, nums):
        self.k = k
        self.num = sorted(nums)

    def add(self, val):
        bisect.insort(self.num, val)

        return self.num[-self.k]
nums = [4,5,8,2]
k = 3
kth_l = KthLargest(k, nums)
print(kth_l.add(3))
print(kth_l.add(5))
print(kth_l.add(10))
print(kth_l.add(9))
print(kth_l.add(4))
