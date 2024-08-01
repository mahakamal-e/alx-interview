N Queens Problem
Description
The N Queens problem involves placing N queens on an N × N chessboard such that no two queens can attack each other. This means no two queens should be in the same row, column, or diagonal.

The provided script, 0-nqueens.py, uses a backtracking algorithm to solve this problem. The algorithm explores all possible placements of queens on the board, ensuring that each placement is valid.

Algorithm
Overview
The backtracking algorithm for the N Queens problem involves the following steps:

Initialization:

Start with an empty chessboard and try to place queens row by row.
Safety Check (is_safe Function):

Ensure that placing a queen in a given position does not result in conflicts with already placed queens. The checks include:
Same column
Major diagonal
Minor diagonal
Recursive Placement (place_queens Function):

Place a queen in each column of the current row.
Recursively try to place queens in the subsequent rows.
Backtrack if placing a queen leads to an invalid configuration.
Base Case:

When all queens are placed (row == N), a valid configuration is found and recorded.
Output:

Each solution is formatted as a list of [row, column] pairs, where each pair represents the position of a queen.
Usage
To use the script, run it with an integer argument N, which specifies the number of queens and the size of the chessboard. The script will output all possible solutions.


