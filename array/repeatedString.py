def brute_force_solution(s, n):

    output = 0

    i = 0
    while i < n:
        for char in s:
            if char == 'a' and i < n:
                output += 1
            elif i > n:
                break
            i += 1

    return output

def better_approach(s, n):

    a_count = s.count('a')
    n_divided_by_s = n // len(s)
    remaining_char = n % len(s)

    a_count_remaining_char = s[:remaining_char].count('a')

    return a_count * n_divided_by_s + a_count_remaining_char

def main():
    s = 'aba'
    n = 10

    res = better_approach(s, n)

    print(res)

if __name__ == "__main__":
    main()