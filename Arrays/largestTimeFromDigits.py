import itertools

def bruteForce(A):
    ans = -1

    for h1, h2, m1, m2 in itertools.permutations(A):

        # convert integer list into string list and join list
        num = int("".join(map(str, [h1, h2, m1, m2])))

        hour = 10 * h1 + h2
        mins = 10 * m1 + m2

        if hour <= 23 and mins < 60 and num > ans:
            ans = num

    if ans == -1:
        return ""

    ans = format(ans, "04")

    return "{}:{}".format(ans[:2], ans[2:])

def largestTimeFromDigits(A):
    c = 2400

    max = float("-inf")
    for i in range(len(A)):
        sum = str(A[i])
        if int(sum) <= 2:
            for j in range(i + 1, len(A)):
                sum = sum + str(A[j])
        sum_val = int(sum)
        if sum_val > max and sum_val < c:
            max = sum_val

    return max

def main():
    nums = [1,2,3,4]
    ret = bruteForce(nums)

    print(ret)


    nums = [0,3,0,0]
    ret = bruteForce(nums)

    print(ret)

if __name__ == "__main__":
    main()