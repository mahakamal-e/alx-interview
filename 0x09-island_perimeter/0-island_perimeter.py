#!/usr/bin/python3
""" island_perimeter Module """


def island_perimeter(grid):
    """ Returns the perimeter of the island. """
    perimeter = 0

    num_rows = len(grid)
    num_cols = len(grid[0])

    for row in range(num_rows):
        for col in range(num_cols):
            if grid[row][col] == 1:
                # Check the top
                if row == 0 or grid[row - 1][col] == 0:
                    perimeter += 1
                # Check the bottom
                if row == num_rows - 1 or grid[row + 1][col] == 0:
                    perimeter += 1
                # Check the left
                if col == 0 or grid[row][col - 1] == 0:
                    perimeter += 1
                # Check the right
                if col == num_cols - 1 or grid[row][col + 1] == 0:
                    perimeter += 1

    return perimeter
