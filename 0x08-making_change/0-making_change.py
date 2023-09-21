#!/usr/bin/python3
"""
0-making_change module
"""


def makeChange(coins, total):
    """Returns a minimum amount of coins needed to make
    a given amount of change

    Args:
        total: The change amount to make
        coins: list of the values of the coins in
        your possession
    Return:
        The fewest number of coins needed to make a
        a given amount total
        if total is 0 or less return 0
        if total can not be met with given the coins
        return -1
    """
    if total <= 0:
        return 0
    table = [float('inf')] * (total + 1)
    table[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            if i - coin >= 0:
                table[i] = min(table[i], table[i - coin] + 1)

    if table[total] == float('inf'):
        return -1
    else:
        return table[total]
