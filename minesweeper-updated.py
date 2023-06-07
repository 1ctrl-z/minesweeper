def minesweeper(grid):
    if not grid or not all(grid):
        raise ValueError("Invalid grid: The grid must be a non-empty 2D list.")

    rows = len(grid)
    cols = len(grid[0])

    for row in grid:
        if len(row) != cols:
            raise ValueError("Invalid grid: All rows must have the same number of columns.")

        for cell in row:
            if cell not in ('#', '-'):
                raise ValueError("Invalid grid: Each cell must be either '#' or '-'.")

    count_grid = [[0] * cols for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '#':
                continue

            for i in range(max(0, r - 1), min(rows, r + 2)):
                for j in range(max(0, c - 1), min(cols, c + 2)):
                    if grid[i][j] == '#':
                        count_grid[r][c] += 1

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '-':
                grid[r][c] = str(count_grid[r][c])

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