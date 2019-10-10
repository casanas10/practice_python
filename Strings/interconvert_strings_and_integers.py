def int_to_string(x):

    is_negative = False

    if x < 0:
        x = -x
        is_negative = True

    s = []
    while True:

        s.append(chr(ord('0') + x % 10))   #chr returns a char from an integer unicode
                                          # ord takes string and returns unicode integer
        x //= 10

        if x == 0:
            break

    return ('-' if is_negative else '') + ''.join(reversed(s))

def string_to_int(str):
    x = 0
    for i, s in enumerate(str):
        x = x * 10 + (ord(s) - ord('0'))

    return x

x = -34366
print(int_to_string(x))

str = "250"
print(string_to_int(str))