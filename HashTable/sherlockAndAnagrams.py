def sherlockAndAnagrams(s):

    map = {}

    count = 0

    for i in range(len(s)):
        for j in range(i+1, len(s) + 1):
            substring_list = list(s[i:j])
            substring_list.sort()

            sorted_string = ''.join(substring_list)

            if sorted_string in map:
                count += map[sorted_string]
                map[sorted_string] += 1
            else:
                map[sorted_string] = 1

    return count

def main():

    # s = "ifailuhkqq"
    # res = sherlockAndAnagrams(s)
    #
    # print(res)
    #
    # s = "kkkk"
    # res = sherlockAndAnagrams(s)
    #
    # print(res)

    s = "cdcd"
    res = sherlockAndAnagrams(s)

    print(res)


if __name__ == "__main__":
    main()