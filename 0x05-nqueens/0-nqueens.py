#!/usr/bin/python3
""" N queen problem """
import sys


def is_safe(board, row, col, N):
    """Check the current column"""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(N):
    """sets up the board and starts the recursive """
    def place_queens(row):
        """place a queen in each row and backtracks if it finds a conflict"""
        if row == N:
            solution = []
            for i in range(N):
                solution.append([i, board[i]])
            solutions.append(solution)
        else:
            for col in range(N):
                if is_safe(board, row, col, N):
                    board[row] = col
                    place_queens(row + 1)

    board = [-1] * N
    solutions = []
    place_queens(0)
    return solutions

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()

