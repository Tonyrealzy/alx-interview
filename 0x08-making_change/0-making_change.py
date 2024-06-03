#!/usr/bin/python3
""" Script that determines the fewest number of
coins needed to meet a given amount total,
given a pile of coins of different values.
"""

def makeChange(coins, total):
    """
    Determines the fewest number of coins needed
    to meet a given amount total, given a pile of
    coins of different values.

    Parameters:
    coins: A list of integers representing the values
    """

    if total <= 0:
        return 0
    
    minCoins = [float('inf')] * (total + 1)
    minCoins[0] = 0

    for currentTotal in range(1, total + 1):
        for coin in coins:
            if coin <= currentTotal:
                remainder = currentTotal - coin
                minCoins[currentTotal] = min(minCoins[currentTotal], minCoins[remainder] + 1)

    return minCoins[total] if minCoins[total] != float('inf') else - 1