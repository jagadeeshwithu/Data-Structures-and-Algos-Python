"""
Determine given input of Sudoku Puzzle is valid or not!

For e.g.,

grid = [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
        ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
        ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
        ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
        ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
        ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
        ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
        ['.', '2', '.', '.', '3', '.', '.', '.', '.']]

the output should be sudoku2(grid) = False, because there are two '1's in the second column

"""


def sudoku2(grid):
    return (is_row_valid(grid) and
            is_col_valid(grid) and
            is_square_valid(grid))


def is_row_valid(grid):
    for row in grid:
        if not is_unit_valid(row):
            return False
    return True


def is_col_valid(grid):
    for col in zip(*grid):
        if not is_unit_valid(col):
            return False

    return True


def is_square_valid(grid):
    for i in (0, 3, 6):
        for j in (0, 3, 6):
            square = [grid[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            if not is_unit_valid(square):
                return False

    return True


def is_unit_valid(unit):
    unit = [i for i in unit if i != '.']
    return len(set(unit)) == len(unit)


if __name__ == "__main__":

    grid = [["7",".",".",".","4",".",".",".","."],
             [".",".",".","8","6","5",".",".","."],
             [".","1",".","2",".",".",".",".","."],
             [".",".",".",".",".","9",".",".","."],
             [".",".",".",".","5",".","5",".","."],
             [".",".",".",".",".",".",".",".","."],
             [".",".",".",".",".",".","2",".","."],
             [".",".",".",".",".",".",".",".","."],
             [".",".",".",".",".",".",".",".","."]]

    print(sudoku2(grid))
