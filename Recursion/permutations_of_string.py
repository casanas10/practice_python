'''
Problem:
Implement a function thall prints all possible orderings of the characters in a string. Print all permuations!!

Example: ABC.
ABC ACB BAC BCA CBA CAB
'''

def permute(s):
    s = list(s)
    def backtrack(first):
        if first == len(s):
            print(''.join(s))
        else:
            for i in range(first, len(s)):
                s[first], s[i] = s[i], s[first]
                backtrack(first + 1)

    backtrack(first=0)

s = "abc"
permute(s)