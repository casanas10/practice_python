def addBinary(a, b):

    a = int(a, 2)
    b = int(b, 2)

    result = bin(a+b)

    return result[2:]

def main():
    a = "11"
    b = "1"

    print(addBinary(a, b))


if __name__ == "__main__":
    main()