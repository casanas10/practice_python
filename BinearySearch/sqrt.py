def sqrt(x):

    if x < 2: return x

    left = 2
    right = x // 2

    while left <= right:
        pivot = left + (right - left) // 2

        num = pivot * pivot

        if x == num:
            return pivot
        elif num > x:
            right = pivot - 1
        else:
            left = pivot + 1

    return right

def main():

    x = 4
    print(sqrt(x))

if __name__ == "__main__":
    main()