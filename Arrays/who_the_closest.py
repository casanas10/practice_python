def closest(s, queries):

    if len(queries) == 0: return [-1]

    closest_indicies = []
    for q in queries:
        min_indx = float('inf')
        min_dist = float('inf')
        for indx,c in enumerate(s):
            if q != indx and s[q] == c and abs(indx - q) < min_dist:
                min_dist = abs(indx - q)
                min_indx = indx

        if min_indx == float('inf'):
            min_indx = -1
        closest_indicies.append(min_indx)

    return closest_indicies

import collections
import bisect
import time

def closest_v2(s, queries):
    map = collections.defaultdict(list)
    for indx, c in enumerate(s):
        map[c].append(indx)

    result = []
    for q in queries:
        if s[q] in map:
            if len(map[s[q]]) == 1:
                result.append(-1)
            else:
                l = map[s[q]]
                res = bisect.bisect_left(l, q)
                left = float('inf')
                right = float('inf')

                if res - 1 >= 0:
                    left = res - 1
                if res + 1 < len(l):
                    right = res + 1

                if left == float('inf') and right != float('inf'):
                    result.append(l[right])
                elif right == float('inf') and left != float('inf'):
                    result.append(l[left])
                else:
                    if abs(l[left] - q) > abs(l[right] - q):
                        result.append(l[right])
                    else:
                        result.append(l[left])

    return result

s = "hhaotakaol"

start = time.time()
print(closest(s, [2,5,7]))
end = time.time()
print(end - start)

start = time.time()
print(closest_v2(s, [2,5,7]))
end = time.time()
print(end - start)

# s = "aaaa"
# # print(closest(s, [0,1,2,3]))
# print(closest_v2(s, [0,1,2,3]))
#
# s = "sam"
# # print(closest(s, [1]))
# print(closest_v2(s, [1]))