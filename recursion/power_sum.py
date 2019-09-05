"""
Find the number of ways integer X can be expressed as sum of 
the Nth powers of unique natural numbers

"""
class Solution:
  	def power_sum(self, X, N):
		return 0

def main():
	assert (Solution().power_sum(X = 10, N = 2) == 1)
	assert (Solution().power_sum(X = 100, N = 2) == 3)
	assert (Solution().power_sum(X = 100, N = 3) == 1)

if __name__ == "__main__":
	main()