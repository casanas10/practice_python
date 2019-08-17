'''
Problem can be found here: https://leetcode.com/problems/container-with-most-water/

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Example:
Input: [1,8,6,2,5,4,8,3,7]
Output: 49

'''

class Solution:
  	def maxArea(self, height):
		i = 0
		j = len(height) - 1
		max_water = 0

		while (i < j):
			max_water = max(max_water, (j-i) * min(height[i], height[j]))
			if height[i] < height[j]:
				i += 1
			else:
				j -= 1
		return max_water

def main():
	height = [1,8,6,2,5,4,8,3,7]
	ret = Solution().maxArea(height)

	print(ret)
	assert(ret == 49), "Answer is incorrect" 

if __name__ == "__main__":
	main()