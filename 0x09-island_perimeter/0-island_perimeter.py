#!/usr/bin/python3
"""
0-island_perimeter problem
"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid
    Args:
        grid: a list of list of ints
            0: represent water
            1: represents land
    Return:
         perimeter of the island described in grid
    """
    row_len = len(grid)
    col_len = len(grid[0])

    p = 0
    conn = 0

    for row in range(row_len):
        for col in range(col_len):
            if grid[row][col] == 1:
                p += 4

                if row != 0 and grid[row - 1][col] == 1:
                    conn += 1
                if col != 0 and grid[row][col - 1] == 1:
                    conn += 1

    return p - (conn * 2)
