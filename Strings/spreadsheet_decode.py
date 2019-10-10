def ss_decode_col_id(str):
    res = 0
    for i, s in enumerate(str):
        res *= 26
        res += ord(s) - ord('A') + 1
    return res

def colnum_string(n):
    string = ""
    while n > 0:
        n, remainder = divmod(n - 1, 26)  # takes 2 numbers and return quotient and remainer
        string = chr(ord('A') + remainder) + string
    return string


str = "ZZ"
print(ss_decode_col_id(str))


str = "AA"
print(ss_decode_col_id(str))

str = "D"
print(ss_decode_col_id(str))


print(colnum_string(702))