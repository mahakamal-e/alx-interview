#!/usr/bin/python3
""" Define minOperations function """


def minOperations(n):
    """
    method that calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            quotient = n // factor
            n = quotient
        factor += 1

    return operations
