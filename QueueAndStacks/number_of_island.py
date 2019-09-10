'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water
and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 2:

Input:
11000
11000
00100
00011

Output: 3

'''

def number_of_islands(grid):

    if not grid: return 0

    count = 0
    visited = [[False for _ in range(len(grid[0]))]for _ in range(len(grid))]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1 and not visited[i][j]:
                DFS(grid, visited, i, j)
                count += 1

    return count

def DFS(grid, visited, i, j):

    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 1 or visited[i][j]:
        return

    visited[i][j] = True

    DFS(grid, visited, i - 1, j)
    DFS(grid, visited, i + 1, j)
    DFS(grid, visited, i, j - 1)
    DFS(grid, visited, i, j + 1)

def main():

    matrix = [
        [1,1,0,0,0],
        [1,1,0,0,0],
        [0,0,1,0,0],
        [0,0,0,1,1]]


    print(number_of_islands(matrix))


if __name__ == "__main__":
    main()