'''
Approach 1 : Brute Force
Time Complexity O(n^3)
Space Complexity O(1)
'''
def lengthOfLongestSubstring(s):
    ans = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if isAllUnique(s, i, j):
                ans = max(ans, j - i)
    return ans

def isAllUnique(s, start, end):
    set_ = set()
    for i in range(start, end):
        if s[i] in set_:
            return False
        else:
            set_.add(s[i])
    return True

'''
Approach 2 - Sliding Window 
Time Complexity: O(n)
Space Complexity : O(1)
'''
def sliding_window(s):
    set_ = set()
    i = 0
    j = 0
    ans = 0

    while (i < len(s) and j < len(s)):
        if s[j] in set_:
            set_.remove(s[i])
            i += 1
        else:
            set_.add(s[j])
            j += 1
            ans = max(ans, j-i)

    return ans


'''
Approach 3 : Optimized Sliding Window
Time Complexity : O(n)
Space Complexity : O(1)
'''
def sliding_window_optimized(s):
    map = {}
    i = 0
    ans = 0
    for j in range(len(s)):
        if s[j] in map:
            i = max(map[s[j]], i)
        ans = max(ans, j - i + 1)
        map[s[j]] = j + 1

    return ans

s = "heomllde"
print(lengthOfLongestSubstring(s))

# s = "pwwkew"
s = "heomllde"
print(sliding_window_optimized(s))