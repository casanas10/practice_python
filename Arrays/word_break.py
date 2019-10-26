# -*- coding: utf-8 -*-
"""
Problem:
Given a string s and a dictionary of words dict, determine if s can be segmented into a 
space-separated sequence of one or more dictionary words. 
Example, 
Input s = “leetcode” ["leet", "code"]
Output True 
because “leetcode” can be segmented as “leet code”.
"""

class Solution:

	# Recursive O(n^2) Solution
	def naive_word_break(self, s, dic):

		if len(s) == 0: return True

		for i in range(1, len(s) + 1):
			sub = s[:i]
			if not sub in dic: continue
			if self.naive_word_break(s[i:], dic):
				return True

		return False

	
  	def word_break_DP(self, s, dic):
  		return False

def main():
	s = "leetcode"
	dic = ["leet", "code"]
	ret = Solution().naive_word_break(s, dic)

	print(ret)

	s = "leetcode"
	dic = ["leet", "code"]
	ret = Solution().word_break_DP(s, dic)

	print(ret)

if __name__ == "__main__":
	main()