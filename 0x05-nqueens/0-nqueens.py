#!/usr/bin/python3
"""
0-nqueens
"""
import sys


def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def place_queen(N):
    board = [[j for j in range(N)] for i in range(N)]

    solutions = []

    def back_track(row):
        if row == N:
            solutions.append([[i, board[i]] for i in range(N)])
            return

        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                back_track(row + 1)
                board[row] = -1

    back_track(0)
    return solutions


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: nqueens N')
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print('{} must be a number'.format(N))
        sys.exit(1)

    if N < 4:
        print('{} must be a number'.format(N))
        sys.exit(1)

    solutions = place_queen(N)
    for solution in solutions:
        print(solution)
