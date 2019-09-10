def daily_temp(T):
    ans = [0] * len(T)
    stack = []  # indexes from hottest to coldest
    for i in range(len(T) - 1, -1, -1):
        while stack and T[i] >= T[stack[-1]]:
            stack.pop()
        if stack:
            ans[i] = stack[-1] - i
        stack.append(i)
    return ans

def main():
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    print(daily_temp(T))


if __name__ == "__main__":
    main()