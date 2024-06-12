#!/usr/bin/python3
"""
A file containing the function def island_perimeter(grid)
that returns the perimeter of the island described in grid
"""

def island_perimeter(grid):
    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                # Check the top
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                # Check the left
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                # Check the bottom
                if i == len(grid) - 1 or grid[i+1][j] == 0:
                    perimeter += 1
                # Check the right
                if j == len(grid[i]) - 1 or grid[i][j+1] == 0:
                    perimeter += 1

    return perimeter