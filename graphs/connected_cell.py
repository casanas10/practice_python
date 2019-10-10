def getRegionSize(grid, r, c):
    # boundary checks
    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
        return 0

    if grid[r][c] == 0:
        return 0

    grid[r][c] = 0  #set loc to 0

    size = 1
    for row in range(r-1, r+2):
        for col in range(c-1, c+2):
            #skip over myself
            if row != r or col != c:
                size += getRegionSize(grid, row, col)

    return size

def getBiggestRegion(grid):

    max_region = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                #do dfs here
                size = getRegionSize(grid, r, c)
                max_region = max(size, max_region)

    return max_region


grid = [
    [0, 0, 0, 1, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0],
    [1, 1, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

print(getBiggestRegion(grid))