#TODO

def longest_string_chain(words):

    hash_table = {}

    words.sort(key=len)

    for w in words:
        for char in w:
            print(char)


    return 0

def process_word(word):

    if len(word) == 1:
        return 1

    stack = []




def main():
    words = ["a","b","ba","bca","bda","bdca"]
    print(longest_string_chain(words))


    words2 = ["i", "as", "sa", "hi", "sash", "ssahi", "sashi", "ashi", "shi"]
    print(longest_string_chain(words2))

if __name__ == "__main__":
    main()