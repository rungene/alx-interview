#!/usr/bin/python3
"""
0-prime_game
"""


def find_prime(num):
    """uses the Sieve of Eratosthenes algorithm to efficiently
    generate a list of prime numbers up to a given number
    Args:
        Number up to which to generate prime numbers
    Returns:
        List of prime numbers
    """
    sieve = [True] * (num + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(pow(num, 0.5)) + 1):
        if sieve[i]:
            for j in range(i * i, num + 1, i):
                sieve[j] = False
    prime_nums = [i for i in range(2, num + 1) if sieve[i]]
    return prime_nums


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
    maria = ben = 0
    for i in range(x):
        if nums[i] == 0:
            continue
        count = len(find_prime(nums[i]))
        if (count % 2) == 0:
            ben += 1
        else:
            maria += 1

    if maria > ben:
        return 'Maria'
    elif maria < ben:
        return 'Ben'
    else:
        return None
