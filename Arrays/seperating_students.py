# def minMoves(students):
#     if len(students) <= 2:
#         return 0
#
#     # calculate moving 0 to right
#     p = 0
#     q = len(students) - 1
#     min_moves = 0
#     while p < q:
#         if students[p] == 0:
#             if students[q] != 1:
#                 q -= 1
#             else:
#                 #swapping
#                 students[p], students[q] = students[q], students[p]
#                 min_moves += 1
#         else:
#             p += 1
#
#     return min_moves

def minMoves(students):

    # Array to store count of zeroes
    zeros_first = 0
    count = 0

    for i in range(len(students) - 1, -1, -1):
        if students[i] == 0:
            count += 1
        else:
            zeros_first += count

    ones_first = 0
    count = 0
    for i in range(len(students) - 1, -1, -1):
        if students[i] == 1:
            count += 1
        else:
            ones_first += count

    return min(zeros_first, ones_first)

students = [1,0,1,0,1,0]
print(minMoves(students))

students = [0,1,0,1]
print(minMoves(students))
#
students = [1,1,1,1,0,0,0,0]
print(minMoves(students))
#
students = [1,1,1,1,0,1,0,1]
print(minMoves(students))

students = [0, 0, 1, 0, 1, 0, 1, 1]
print(minMoves(students))