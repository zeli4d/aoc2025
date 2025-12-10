import copy
from itertools import repeat


def a():
    result = 0

    grid = []
    with open("input04.txt") as f:
        for line in f:
            grid.append(list(line.strip()))

    # for ln in grid:
    #     print(''.join(ln))

    # grid2 = copy.deepcopy(grid)
    rows = len(grid)
    columns = len(grid[0])
    print("rows = ", rows, ", columns = ", columns)
    for row in range(rows):
        for col in range(columns):
            nbrs = 0
            # print(row, col)
            if grid[row][col] == "@":
                if row > 0 and col > 0 and grid[row - 1][col - 1] == "@":
                    nbrs += 1
                if row > 0 and grid[row - 1][col] == "@":
                    nbrs += 1
                if row > 0 and col < columns - 1 and grid[row - 1][col + 1] == "@":
                    nbrs += 1
                if col > 0 and grid[row][col - 1] == "@":
                    nbrs += 1
                if col < columns - 1 and grid[row][col + 1] == "@":
                    nbrs += 1
                if row < rows - 1 and col > 0 and grid[row + 1][col - 1] == "@":
                    nbrs += 1
                if row < rows - 1 and grid[row + 1][col] == "@":
                    nbrs += 1
                if row < rows - 1 and col < columns - 1 and grid[row + 1][col + 1] == "@":
                    nbrs += 1

                if nbrs < 4:
                    result += 1
                    # grid2[row][col] = "x"

    # for ln in grid2:
    #     print(''.join(ln))

    print("result(a) = ", result)


def b():
    result = 0

    grid = []
    with open("input04.txt") as f:
        for line in f:
            grid.append(list(line.strip()))

    # for ln in grid:
    #     print(''.join(ln))

    grid2 = copy.deepcopy(grid)
    rows = len(grid)
    columns = len(grid[0])
    print("rows = ", rows, ", columns = ", columns)

    removed = 1
    while (removed>0):
        removed = 0
        grid = copy.deepcopy(grid2)
        for row in range(rows):
            for col in range(columns):
                nbrs = 0
                # print(row, col)
                if grid[row][col] == "@":
                    if row > 0 and col > 0 and grid[row - 1][col - 1] == "@":
                        nbrs += 1
                    if row > 0 and grid[row - 1][col] == "@":
                        nbrs += 1
                    if row > 0 and col < columns - 1 and grid[row - 1][col + 1] == "@":
                        nbrs += 1
                    if col > 0 and grid[row][col - 1] == "@":
                        nbrs += 1
                    if col < columns - 1 and grid[row][col + 1] == "@":
                        nbrs += 1
                    if row < rows - 1 and col > 0 and grid[row + 1][col - 1] == "@":
                        nbrs += 1
                    if row < rows - 1 and grid[row + 1][col] == "@":
                        nbrs += 1
                    if row < rows - 1 and col < columns - 1 and grid[row + 1][col + 1] == "@":
                        nbrs += 1

                    if nbrs < 4:
                        result += 1
                        grid2[row][col] = "."
                        removed += 1

    # for ln in grid2:
    #     print(''.join(ln))

    print("result(a) = ", result)


# a()
b()
