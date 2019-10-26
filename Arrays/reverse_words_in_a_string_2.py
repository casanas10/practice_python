'''
Given an input string , reverse the string word by word.

Example:

Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
Note:
A word is defined as a sequence of non-space characters.
The input string does not contain leading or trailing spaces.
The words are always separated by a single space.
'''


def reverse(str, i, j):
    if len(str) == 0: return
    while (i < j):
        temp = str[i]
        str[i] = str[j]
        str[j] = temp

        i += 1
        j -= 1

    return str

def reverse_words(str):

    i = 0
    j = len(str) - 1

    reverse(str, i, j)
    str.append(" ")

    i = 0
    for j in range(len(str)):
        if str[j] == " ":
            reverse(str, i, j - 1)
            i = j+1

    str.pop()
    return str

def main():
    str = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
    print(reverse_words(str))
if __name__ == "__main__":
    main()