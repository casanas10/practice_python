from collections import deque

def isValid(grid, r, c):
    return r >= 0 and c >= 0 and r < len(grid) and c < len(grid[0])


def bfs(grid, r, c):

    queue = [(r,c)]

    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    grid[r][c] = 0

    while queue:
        r,c = queue.pop(0)
        for d in directions:
            nr = r + d[0]
            nc = c + d[1]
            if isValid(grid, nr, nc) and grid[nr][nc] == 1:
                queue.append((nr, nc))
                grid[nr][nc] = 0


def numOfIslandsBFS(grid):

    if not grid or grid == [[]]:
        return 0

    islands = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                islands += 1
                bfs(grid, r, c)

    return islands

def numOfIslandsDFS(grid):
    def dfs(grid, r, c):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0:
            return

        grid[r][c] = 0
        dfs(grid, r - 1, c)
        dfs(grid, r + 1, c)
        dfs(grid, r, c - 1)
        dfs(grid, r, c + 1)

    if not grid or grid == [[]]:
        return 0

    islands = 0

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == 1:
                islands += 1
                dfs(grid, r, c)

    return islands


####DFS

print("#DFS")
grid = [
    [1, 1, 1],
    [0, 1, 0],
    [1, 0, 0],
    [1, 0, 1]
]
print(numOfIslandsDFS(grid))

grid = [[]]
print(numOfIslandsDFS(grid))

grid = None
print(numOfIslandsDFS(grid))

grid = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]
print(numOfIslandsDFS(grid))

####BFS
print("#BFS")

grid = [
    [1, 1, 1],
    [0, 1, 0],
    [1, 0, 0],
    [1, 0, 1]
]
print(numOfIslandsBFS(grid))

grid = [[]]
print(numOfIslandsBFS(grid))

grid = None
print(numOfIslandsBFS(grid))

grid = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]
print(numOfIslandsBFS(grid))