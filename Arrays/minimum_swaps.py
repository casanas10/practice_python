def minimum_swaps(arr, n):

    count = 0

    temp = {a: i for i, a in enumerate(arr)}

    for i in range(len(arr)):
        actual = arr[i]
        expected = i + 1
        if actual != expected:
            t = actual
            arr[i] = expected
            arr[temp[expected]] = t
            temp[t] = temp[expected]
            count += 1

    return count


def main():
    n = 7
    arr = [7,1,3,2,4,5,6]
    res = minimum_swaps(arr, n)

    print(res)

if __name__== "__main__":
    main()