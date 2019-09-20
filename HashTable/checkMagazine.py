def checkMagazine(magazine, note):
    dict = {}
    for word in magazine:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1

    for word in note:
        if word not in dict:
            print("No")
            return
        else:
            occurences = dict[word]
            if occurences == 1:
                del dict[word]
            else:
                dict[word] -= 1
    print("Yes")
    return

def main():

    magazine = "give me one grand today night"
    note = "give one grand today"
    res = checkMagazine(magazine, note)

if __name__ == "__main__":
    main()