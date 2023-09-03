#!/usr/bin/python3
"""
0-nqueens
"""
import sys

nqueens = None
if len(sys.argv) < 2:
    print('Usage: {} <queens'.format(sys.argv[0]))
    sys.exit(1)

queens = sys.argv[1]
try:
    queens = int(queens)
    if queens < 4:
        print('{} must be at least 4'.format(queens))
        sys.exit(1)
    nqueens = queens
except ValueError:
    print('{} must be a number'.format(queens))
    sys.exit(1)

current_solution = [0 for i in range(nqueens)]
solutions = []


def is_safe(test_row, test_col):
    """Checks if it is safe to place a queen"""
    # no need to check for row 0
    if test_row == 0:
        return True

    for row in range(0, test_row):
        # Check vertical
        if test_col == current_solution[row]:
            return False

        # diagonal
        if abs(test_row - row) == abs(test_col - current_solution[row]):
            return False

    # no attack found
    return True


def place_queen(row):
    global current_solution, solutions, nqueens

    for col in range(nqueens):
        if not is_safe(row, col):
            continue
        else:
            current_solution[row] = col
            if row == (nqueens - 1):
                # last row
                solutions.append(current_solution.copy())
            else:
                place_queen(row + 1)


place_queen(0)
for solution in solutions:
    print(solution)
