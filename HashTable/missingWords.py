def missingWords(s, t):

    st = set()
    for word in t.split(" "):
        st.add(word)

    output = []

    for word in s.split(" "):
        if word in st:
            st.remove(word)
        else:
            output.append(word)

    return output

def solution(s, t):

    missing = []
    a = s.split()
    b = t.split()

    j = 0
    for i in range(a):
        if a[i] != b[j]:
            missing.append(a[i])
        else:
            j += 1

    return missing

def main():

    s = "I like eating cheese do you like cheese"
    t = "like cheese"
    res = solution(s, t)

    print(res)

    s = ""
    t = "HackerRank to practice"
    res = solution(s, t)

    print(res)

if __name__ == "__main__":
    main()