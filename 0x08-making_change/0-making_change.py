#!/usr/bin/python3
"""Make Change"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given `total`.

    Args:
        coins (list of int): A list of coin denominations.
        total (int): The total amount to be made change.

    Returns:
        int: The minimum number of coins needed to make `total`,
        or -1 if it's not possible to make change.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    no_coins = 0

    for coin in coins:
        count = total // coin
        no_coins += count
        total -= count * coin

    return no_coins if total == 0 else -1
