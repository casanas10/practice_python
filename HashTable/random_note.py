'''
Given an anonymous letter and a text from a megazine. Write a function that determines if the anonymous letter can be constructed from the magazine

Constraints:
Each letter in the magazine can only be used once in your random note.

Examples:
canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
'''

import collections

'''
Time Complexity : O(n+m) worst case, letter is not constructible or need the last letter of the magazine
m and n are the number of characters in the letter and magazine

Space Complexity : O(L) size of the hashtable over the letter L is the distinct characters appearing in the letter

If the letters are coded in ASCII we could use a 256 entry integer array with A[i] being the number of times character i appears in the letter 
If only lowercase English letter than we can use an array of size 26 

'''
def canConstruct(ransomNote, magazine):

    if len(ransomNote) == 0: return True

    note_map_counter = collections.Counter(ransomNote)

    for i in magazine:
        if i in note_map_counter:
            note_map_counter[i] -= 1

            if note_map_counter[i] == 0:
                del note_map_counter[i]
                if len(note_map_counter) == 0:
                    return True

    return False

def canConstructApproach2(ransomNote, magazine):

    i = 0
    while i < len(ransomNote):
        if ransomNote[i] not in magazine:
            return False
        magazine = magazine.replace(ransomNote[i], "", 1)
        i+= 1
    return True

def canConstructApproach3(ransomNote, magazine):
    return not collections.Counter(ransomNote) - collections.Counter(magazine)

#Approach 1 My
note = "money"
magazine = "mlloadfdeoyasdflkasdflkwqeurpommqiwrnasfd"
print(canConstruct(note, magazine))

note = "money"
magazine = "myltop"
print(canConstruct(note, magazine))

#Approach 2
note = "money"
magazine = "mlloadfdeoyasdflkasdflkwqeurpommqiwrnasfd"
print(canConstructApproach2(note, magazine))

note = "money"
magazine = "myltop"
print(canConstructApproach2(note, magazine))

#Approach 3
note = "money"
magazine = "mlloadfdeoyasdflkasdflkwqeurpommqiwrnasfd"
print(canConstructApproach3(note, magazine))

note = "money"
magazine = "myltop"
print(canConstructApproach3(note, magazine))
