'''
Problem check permutation
Given 2 strings, write a method to decide if one is a permutation of the other

'''


def naive_check_permutation(str1, str2):

    if len(str1) != len(str2):
        return False

    for i in str1:
        if i not in str2:
            return False

    return True

def hashmap_check_permutation(str1, str2):

    if len(str1) != len(str2):
        return False

    dict = {}
    for i in str1:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1

    for i in str2:
        if i in dict:
            if dict[i] > 1:
                dict[i] -= 1
            else:
                del dict[i]
        else:
            return False

    return True

'''
Another solution is to sort the 2 strings -> 
takes O(n log n) time and O(n) space then compare both strings
'''

def main():

    str1 = "hello"
    str2 = "elloh"

    ret = hashmap_check_permutation(str1, str2)
    print(ret)

    str1 = "hellp"
    str2 = "elloh"

    ret = hashmap_check_permutation(str1, str2)
    print(ret)

if __name__ == "__main__":
    main()
