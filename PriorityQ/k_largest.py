import heapq

def kLargest(nums, k):

    heapq._heapify_max(nums)

    i = 1
    while nums:
        val = heapq._heappop_max(nums)
        if i == k:
            return val
        i += 1

    return -1

def optimalSolution(nums, k):
    n_largest = heapq.nlargest(k, nums)
    return n_largest[-1]

def main():

    nums = [3,2,1,5,6,4]
    k = 2
    print(kLargest(nums, k))

    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(optimalSolution(nums, k))


if __name__ == "__main__":
    main()