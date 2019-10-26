import math

def nThUglyNumber(n,a,b,c):

    #least common multiple
    def lcm(x, y):
        return x * y // math.gcd(x, y)

    ab, bc, ac = lcm(a, b), lcm(b, c), lcm(c, a)
    abc = lcm(ab, c)
    low = 1
    high = 2 * 10 ** 9
    while low < high:
        mid = low + (high - low) // 2
        cnt = mid // a + mid // b + mid // c - mid // ab - mid // bc - mid // ac + mid // abc
        if cnt < n:
            low = mid + 1
        else:
            high = mid
    return low

n = 3
a = 2
b = 3
c = 5
print(nThUglyNumber(n,a,b,c))