'''
O(s * t)
'''
def simple_algorithm(s, t):

    return any(s==t[i:i+len(s)] for i in range(len(t) - len(s)))

def rabin_karp(pattern, text):

    p_len = len(pattern)
    t_len = len(text)

    

def main():

    s1 = "alex"
    s2 = "hello world my name is alejandro"
    res = simple_algorithm(s1, s2)

    print(res)

if __name__ == "__main__":
    main()