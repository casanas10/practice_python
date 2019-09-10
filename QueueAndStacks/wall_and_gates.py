'''
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example:

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
'''


import collections

def wall_and_gates(rooms):

    if not rooms: return

    EMPTY = 2 ** 31 - 1
    GATE = 0
    DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    queue = collections.deque([])

    #find the gates
    for i in range(len(rooms)):
        for j in range(len(rooms[i])):
            if rooms[i][j] == GATE:
                queue.append((i, j))

    # apply BFS from every gate
    while queue:

        point = queue.popleft()

        for d in DIRECTIONS:
            x, y = point

            r = x + d[0]
            c = y + d[1]

            m = len(rooms) - 1
            n = len(rooms[0]) - 1

            if r < 0 or r > m or c < 0 or c > n or rooms[r][c] != EMPTY:
                continue
            else:
                rooms[r][c] = rooms[x][y] + 1
                queue.append((r, c))

    return rooms

def main():

    inf = 2 ** 31 - 1
    matrix = [
        [inf,-1, 0, inf],
        [inf, inf,inf, -1],
        [inf,  -1, inf,  -1],
        [0,  -1, inf, inf]]

    print(wall_and_gates(matrix))


if __name__ == "__main__":
    main()
