# Complete the hourglassSum function below.
def hourglassSum(arr):
    max_sum = float('-inf')

    DIRECTIONS = [(0, 0), (0, 1), (0, 2), (1, 1), (2, 0), (2, 1), (2, 2)]

    r = len(arr)
    c = len(arr[0])

    if r < 3 or c < 3: return -1

    for i in range(r-2):
        for j in range(c-2):
            s = 0
            for d in DIRECTIONS:
                x = i + d[0]
                y = j + d[1]

                s += arr[x][y]

            max_sum = max(max_sum, s)

    return max_sum

def another_solution(arr):

    r = len(arr)
    c = len(arr[0])

    if r < 3 or c < 3: return -1

    #loop (R-2) * (C-2) times

    max_sum = float("-inf")
    for i in range(r-2):
        for j in range(c-2):
            top = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            middle = arr[i+1][j+1]
            bottom = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            sum = top + middle + bottom

            max_sum = max(max_sum, sum)

    return max_sum

def main():
    matrix = [
        [-9, -9, -9,  1, 1, 1],
        [0, -9,  0,  4, 3, 2],
        [-9, -9, -9,  1, 2, 3],
        [0,  0,  8,  6, 6, 0],
        [0,  0,  0, -2, 0,0],
        [0,  0,  1,  2, 4, 0]
    ]

    res = hourglassSum(matrix)

    print(res)

if __name__=="__main__":
    main()