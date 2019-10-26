def brute_force_solution(c):

    output = 0

    i = 0

    while i + 2 < len(c):

        if c[i+2] == 1:
            i += 1
            output += 1
        else:
            i += 2
            output += 1

    if i < len(c) - 1:
        output += 1

    return output

def main():
    c = [0, 0, 1, 0, 0, 1, 0]
    res = brute_force_solution(c)
    print(res)

    c = [0, 0, 0, 1, 0, 0]
    res = brute_force_solution(c)
    print(res)

if __name__ == "__main__":
    main()