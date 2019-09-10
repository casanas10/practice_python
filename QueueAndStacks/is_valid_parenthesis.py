
def isValid(s):

    stack = []

    for i in s:

        if not stack:
            stack.append(i)
        elif i == "]" and stack[-1] == "[":
            stack.pop()
        elif i == "}" and stack[-1] == "{":
            stack.pop()
        elif i == ")" and stack[-1] == "(":
            stack.pop()
        else:
            stack.append(i)

    return not stack


def main():
    s = "[()}]"
    print(isValid(s))


if __name__ == "__main__":
    main()