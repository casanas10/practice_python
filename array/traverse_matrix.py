import collections

def diagonalTraverse(matrix):

    result = []
    dd = collections.defaultdict(list)

    if not matrix: return result

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            sum_index = i + j
            if sum_index % 2 == 0:
                dd[sum_index].insert(0, matrix[i][j])
            else:
                dd[sum_index].append(matrix[i][j])

    for k in dd.keys():
        result += dd[k]

    return result

def main():
    matrix = [
             [ 1, 2, 3 ],
             [ 4, 5, 6 ],
             [ 7, 8, 9 ]
            ]
    print(diagonalTraverse(matrix))


if __name__ == "__main__":
    main()