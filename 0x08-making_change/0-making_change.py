#!/usr/bin/python3
""" Define Make_change function """


def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to meet the total amount.

    Parameters:
    - coins: List of integers representing the coin denominations.
    - total: Integer representing the total amount to be achieved.

    Returns:
    - Integer representing the fewest number of coins needed to meet the total.
    - If total is 0 or less, returns 0.
    - If total cannot be met by any combination of coins, returns -1.
    """
    if total < 1:
        return 0

    coins.sort(reverse=True)
    count = 0

    for coin in coins:
        if total == 0:
            break
        num = total // coin
        total -= num * coin
        count += num

    return count if total == 0 else -1
