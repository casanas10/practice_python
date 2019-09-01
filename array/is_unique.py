'''
Problem is unique
Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

'''

'''compare every char of string to every other char of string 
O(n^2) time
O(1) space
'''
def naive_is_unique(str):
    for i in range(len(str)):
        for j in range(i+1, len(str)-1):
            if str[i] == str[j]:
                return False

    return True

'''hashmap implementation (dictionary)
O(n) time
O(n) space
'''

def hashmap_impl_is_unique(str):
    letters = {}
    for c in str:
        if c in letters:
            return False
        else:
            letters[c] = True
    return True

'''array of boolean values with flag
O(n) time  --- you can argue time complexity is O(c) where c is max size of ascii character
O(1) space
'''

def boolean_array_is_unique(str):
    if len(str) > 256:  # assume ASCII extended
        return False
    bitmap = [False for _ in range(256)]
    for c in str:
        if bitmap[ord(c)]:
            return False
        else:
            bitmap[ord(c)] = True
    return True


'''Use sets to check if any char were deleted
O(n) time
O(n) space
'''
def sets_is_unique(str):

    size = len(str)
    size_set = len(set(str))

    if size == size_set:
        return True

    return False

'''
Other options 
1. Sort and check adjacent chars (sorting takes O(n log n) time and O(n) space)
'''


def main():

    testing_params = [
        "hello",
        "alex",
        "hasdflo"
    ]

    functions = [
        naive_is_unique,
        hashmap_impl_is_unique,
        boolean_array_is_unique,
        sets_is_unique
    ]

    for i in functions:
        for j in testing_params:
            print(i, j, i(j))

if __name__ == "__main__":
    main()
