##Coin Change Problem
###Overview
The goal of this project is to determine the fewest number of coins needed to meet a given total amount, given a pile of coins of different values. The solution should be implemented using the greedy algorithm, which is suitable when coin denominations are such that a locally optimal choice leads to a globally optimal solution.

###Requirements
coins: A list of positive integers representing the values of the coins available. You have an infinite number of each denomination.
total: An integer representing the amount of money to be made.
Approach

###Greedy Algorithm
The greedy algorithm attempts to solve the problem by always picking the largest coin denomination that does not exceed the remaining amount. This approach works optimally in cases where the denominations of the coins ensure that each local optimum is also a global optimum. For example:

Sort the coin denominations in descending order.
Iteratively subtract the largest coin denomination from the total amount until the amount is reduced to zero or it becomes impossible to meet the total with the remaining denominations.
