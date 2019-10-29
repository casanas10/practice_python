'''
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
'''
def toLowerCase(str):
    new_str = []  # list to store lower case char

    for c in str:
        if "A" <= c <= "Z":  # check whether the char is uppercase
            unicode = ord(c) + 32  # add 32 unicode value to it
            char = chr(unicode)  # convert into Char
            new_str.append(char)
        else:
            new_str.append(c)  # add to list as it is in lowercase

    return "".join(new_str)


str = "HEllo"
print(toLowerCase(str))