def minesweeper(grid):
    """
    The function takes a grid as input and replaces all '-' characters with the number of adjacent '#'
    characters in the grid.
    
    :param grid: a 2D list representing the minesweeper game board, where each element is either a '#'
    (representing a mine) or a '-' (representing an empty space)
    :return: The function `minesweeper` returns the updated `grid` with the number of mines adjacent to
    each empty cell represented by a number.
    """
    rows = len(grid)
    cols = len(grid[0])
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col == '-':
                count = 0
                for i in range(max(0, r - 1), min(rows, r + 2)):
                    for j in range(max(0, c - 1), min(cols, c + 2)):
                        if grid[i][j] == '#':
                            count += 1
                grid[r][c] = str(count)
    return grid

grid = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"]
]

result = minesweeper(grid)
print('[')
for r in result:
    print('\t',r)
print(']')