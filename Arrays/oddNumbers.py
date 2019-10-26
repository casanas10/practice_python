def oddNumbers(l, r):
    res = []
    for i in range(l, r + 1):
        if i % 2 != 0:
            res.append(i)

def main():

    l = 3
    r = 9

    res = oddNumbers(l, r)

    print(res)

if __name__ == "__main__":
    main()

'''
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    r = int(input().strip())

    res = oddNumbers(l, r)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
'''