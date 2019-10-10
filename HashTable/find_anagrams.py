import collections

'''
input: set of words 
output: groups of anagrams

Restrictions:
Each group must contain at least 2 words
'''


'''
Time Complexity : O(n m log m) - because we have to go through each word in the dictionary and sort it
- n number of words in the dictionary
- m is the maximum length of a word in dictionary

Space Complexity : O(nm) - because we need to store all the words in the dictionary and the total length of word
'''
def find_anagrams(dictionary):

    map = collections.defaultdict(list)
    #loop over dictionary
    for word in dictionary:
        # sort each word
        #use hashmap to keep track and check if the words are anagrams
        map[tuple(sorted(word))].append(word)

    group = []
    for v in map.values():
        if len(v) >= 2:
            group.append(v)

    #return group of words
    return group



'''
Time Complexity : O(nm) - because we have to go through each word once and then go throguh each char once
- n number of words
- m is the maximum length of a word in dictionary

Space Complexity : O(nm) - because we need to store all characters 26 for each word and all the words in the dict
'''
def find_anagrams_by_count(dictionary):
    map = collections.defaultdict(list)

    for word in dictionary:
        count = [0] * 26
        for c in word:
            count[ord(c) - ord('a')] += 1
        map[tuple(count)].append(word)

    group = []
    for v in map.values():
        if len(v) >= 2:
            group.append(v)

    # return group of words
    return group

dict = ["debitcard", "elvis", "silent", "badcredit", "lives", "freedom", "listen", "levis", "money"]
print(find_anagrams(dict))

print(find_anagrams_by_count(dict))




