#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    list of lists of integers representing the Pascal’s triangle

    Parameters:
        n: int
            num of rows

    Return:
         a list of lists of integers
    """
    res = []
    if n <= 0:
        return res

    pas = [[1]]
    for i in range(n-1):
        temp = [0] + pas[-1] + [0]
        row = []
        for j in range(len(pas[-1]) + 1):
            row.append(temp[j] + temp[j+1])
        pas.append(row)
    return(pas)
