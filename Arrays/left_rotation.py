def solution(n,d, arr):

    sol = [0] * n

    for i in range(len(arr)):

        index = i + n - d

        if index > n - 1:
            index = index % n

        sol[index] = arr[i]

    return sol


def main():
    n = 5
    d = 4
    arr = [1,2,3,4,5]
    res = solution(n, d, arr)

    print(res)

if __name__ == "__main__":
    main()