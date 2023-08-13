#!/usr/bin/python3
"""
0-minoperations
"""


def minOperations(n):
    """
    Given a number 'n', calculates and returns
    the minimum number of operations.
    if n is impossile to achive retun 0
    """
    if n == 1:
        return 0
    res = 0
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            res += i
            n = n // i
    if n > 1:
        res += n
    return res
