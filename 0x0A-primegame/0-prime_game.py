#!/usr/bin/python3
"""
0-prime_game
"""


def is_prime(num):
    """Checks if number is prime
    Args:
        Number to check
    Returns:
        True if the number is prime, false if not
    """
    if num <= 1:
        return False
    if num == 2:
        return True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    """Checks for prime numbers in set
    removes that number and its multiples from the set.
    The player that cannot make a move loses the game.
    The player is unable to make the move if there no
    prime numbers in a set.
    Args:
        x: int number of rounds game can be played
        nums: An array of n. Consecutive inst range
        from 1 to n
    Returns:
        name of the player that won the most rounds
        If the winner cannot be determined, return None
    """
    if not nums or x <= 0:
        return None

    def game_round(nums):
        for num in sorted(nums):
            if is_prime(num):
                return num
        return None
    maria = 0
    ben = 0
    for _ in range(x):
        chosen_num = game_round(nums)
        if not chosen_num:
            return None
        nums = [num for num in nums if num % chosen_num != 0]
        if _ % 2 == 0:
            maria += 1
        else:
            ben += 1
    if maria > ben:
        return 'Winner: Maria'
    elif maria < ben:
        return 'Winner: Ben'
    else:
        return None
