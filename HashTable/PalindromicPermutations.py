import collections

'''
A palindrome is a string that reads the same forwards and backwards "level", "rotator", etc. 
Write a program to check whether the letters in string can be permuted to form a palindrome. For
example: edified can be permuted to deified
'''


'''
Brute force solution will be iterate through all permutations of the strings then check if is a palindrome 
this has a O(2^n) time complexity. 

Another Approach - we notice that all characters must occur in pairs for a string to be a palindrome with exception of odd length string. 
Ex: edified has two e's, two d's, two i's and one f -> this tells us that edified can be permuted into a palindrome 

we can use a hash table mapping characters to frequencies  
'''
def can_form_palindrome(s):
    freq_map = collections.Counter(s)
    sum = 0
    for v in freq_map.values():
        sum += v % 2
    return sum <= 1

s = "edified"
print(can_form_palindrome(s))

s = "oattdat"
print(can_form_palindrome(s))

s = "eevll"
print(can_form_palindrome(s))