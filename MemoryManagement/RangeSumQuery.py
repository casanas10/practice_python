class NumArray:

    def __init__(self, nums):
        self.nums = nums
        self.map = {}
        self.sums = [0] * (len(nums) + 1)

        self.preComputerSumRanges()
        self.preComputeSumRangesConstantTime()

    #Approach 1 Linear Time Constant Space
    def sumRange(self, i, j):
        sum = 0
        for x in range(i, j + 1):
            sum += self.nums[x]

        return sum

    def constantTimeSumRange(self, i, j):
        return self.map[(i, j)]

    # Approach 2 Constant time Quadratic Space
    def preComputerSumRanges(self):
        for i in range(len(self.nums)):
            sum = 0
            for j in range(i, len(self.nums)):
                sum += self.nums[j]
                self.map[(i, j)] = sum

    # Approach 3 Constant Time Linear Space
    def preComputeSumRangesConstantTime(self):

        for i in range(len(self.nums)):
            self.sums[i+1] = self.sums[i] + self.nums[i]

    def lookUpSumRange(self, i, j):
        return self.sums[j+1] - self.sums[i]

# Your NumArray object will be instantiated and called as such:
nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
param_1 = obj.sumRange(2, 5)

print(param_1)

sum = obj.constantTimeSumRange(2, 5)
print(sum)

sum = obj.lookUpSumRange(2, 5)
print(sum)