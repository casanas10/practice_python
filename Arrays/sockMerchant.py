def brute_force_solution(n, arr):

    output = 0

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] != -1 and arr[i] == arr[j]:
                output += 1
                arr[i] = -1
                arr[j] = -1

    return output

def set_solution(n, arr):

    output = 0

    s = set()

    for i in range(len(arr)):
        if arr[i] not in s:
            s.add(arr[i])
        else:
            output +=1
            s.remove(arr[i])

    return output

def main():
    n = 9
    arr = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    res = set_solution(n, arr)

    print(res)

if __name__ == "__main__":
    main()