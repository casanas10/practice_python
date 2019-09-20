def twoStrings(s1, s2):

    s = set()

    for char in s1:
        s.add(char)

    for char in s2:
        if char in s:
            return "YES"

    return "NO"

def main():

    s1 = "hello"
    s2 = "world"
    res = twoStrings(s1, s2)

    print(res)

    s1 = "hi"
    s2 = "world"
    res = twoStrings(s1, s2)

    print(res)

if __name__ == "__main__":
    main()