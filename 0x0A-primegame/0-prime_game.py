#!/usr/bin/python3
""" Module """


def sieve_of_eratosthenes(max_n):
    """ get the prim using sieve algorithm """
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False

    p = 2
    while (p * p <= max_n):
        if primes[p]:
            for i in range(p * p, max_n + 1, p):
                primes[i] = False
        p += 1
    return primes


def isWinner(x, nums):
    """ returns the winner """
    if x <= 0 or not nums:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 1:
            ben_wins += 1
            continue

        num_primes = sum(primes[:n + 1])

        if num_primes % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
