# Min Operations to Achieve n H Characters

This project aims to solve the problem of calculating the fewest number of operations needed to result in exactly  H characters in a text file. The only operations allowed are Copy All and Paste.

## Problem Description

Given a number , write a method  that calculates the fewest number of operations needed to result in exactly  H characters in the file.

### Operations Allowed

1. **Copy All**: Copies all the characters currently in the file.
2. **Paste**: Pastes the last copied characters into the file.

### Example

For :

H => Copy All => Paste => HH => Paste => HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH
