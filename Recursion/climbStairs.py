# Top down - TLE
def climbStairs1(self, n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return self.climbStairs(n-1)+self.climbStairs(n-2)


# Bottom up, O(n) space
def climbStairs2(self, n):
    if n == 1:
        return 1
    res = [0 for i in range(n)]
    res[0], res[1] = 1, 2
    for i in range(2, n):
        res[i] = res[i - 1] + res[i - 2]
    return res[-1]


# Bottom up, constant space
def climbStairs3(self, n):
    if n == 1:
        return 1
    a, b = 1, 2
    for i in range(2, n):
        tmp = b
        b = a + b
        a = tmp
    return b


# Top down + memorization (list)
def climbStairs4(self, n):
    if n == 1:
        return 1
    dic = [-1 for i in range(n)]
    dic[0], dic[1] = 1, 2
    return self.helper(n - 1, dic)


def helper(self, n, dic):
    if dic[n] < 0:
        dic[n] = self.helper(n - 1, dic) + self.helper(n - 2, dic)
    return dic[n]



def climbStairs(n):
    cache = {}
    def helper(n):
        if n == 1: return 1
        if n == 2: return 2

        if n in cache.keys():
            return cache[n]

        result = helper(n - 1) + helper(n - 2)
        cache[n] = result
        return result

    return helper(n)

def main():
    print(climbStairs(3))


if __name__ == "__main__":
    main()