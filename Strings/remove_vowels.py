'''
Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.



Example 1:

Input: "leetcodeisacommunityforcoders"
Output: "ltcdscmmntyfrcdrs"
Example 2:

Input: "aeiou"
Output: ""
'''

def removeVowels(str):

    output = []
    vowels = set(["a", "e", "i", "o", "u"])

    for char in str:
        if char not in vowels:
            output.append(char)

    return "".join(output)

str = "leetcodeisacommunityforcoders"
print(removeVowels(str))
assert removeVowels(str) == "ltcdscmmntyfrcdrs"