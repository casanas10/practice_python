def reverse_string(s):
    i = 0
    j = len(s) - 1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    return s


s = ["h","e","l", "l", "o"]
print(reverse_string(s))

s = ["h","e","l", "l", "o", "k"]
print(reverse_string(s))
