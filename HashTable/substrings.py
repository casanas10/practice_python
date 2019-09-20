def isVowel(char):
    if char in ['a', 'e', 'o', 'i', 'u']:
        return True
    else:
        return False

def findSubstrings(s):

    arr = []

    max_length = float('-inf')
    min_length = float('inf')

    max_arr = []
    min_arr = []

    for i in range(len(s)):
        if isVowel(s[i]):
            for j in range(i+1, len(s)+1):
                substring = s[i:j]
                if len(substring) >= 2 and isVowel(substring[0]) and not isVowel(substring[-1]):

                    if len(substring) >= max_length:
                        max_length = len(substring)
                        if max_arr > substring:
                            max_arr.append(substring)
                    if len(substring) <= min_length:
                        min_length = len(substring)

                        min_arr.append(substring)


    min_arr.sort()
    print(min_arr[0])
    print(max_arr[-1])

def main():

    # s = "rejhiuecumovsutyrulqaeuouiecodjlmjeaummaoqkexylwaaopnfvlbiiiidyckzfhe"
    # res = findSubstrings(s)
    #
    # print(res)
    #
    # s = "abc"
    # res = findSubstrings(s)
    #
    # print(res)

    s = "aab"
    res = findSubstrings(s)

    print(res)


if __name__ == "__main__":
    main()