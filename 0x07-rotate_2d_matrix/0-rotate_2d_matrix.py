#!/usr/bin/python3
"""
0-rotate_2d_matrix module : rotate n*n 2D matrix 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate n*n 2D matrix 90 degrees clockwise

    Args:
        matrix: provided 2d matrix
    Return:
        None
    """
    len_matrix = len(matrix)
    for row in range(len_matrix):
        for col in range(row, len_matrix):
            matrix[row][col], matrix[col][row] = \
                matrix[col][row], matrix[row][col]

    for i in range(len_matrix):
        matrix[i] = matrix[i][::-1]
