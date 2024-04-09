#!/usr/bin/python3
"""_summary_"""

def pascal_triangle(n):
    """This function returns a list of lists representing Pascal's triangle of n rows.
    
    Parameters:
    n: An integer representing the number of rows in the Pascal's triangle.
    
    Returns:
    A list of lists representing Pascal's triangle. Returns an empty list if n <= 0.
    """
    triangle = []
    
    # Building the triangle row by row
    for i in range(n):
        row = []
        for j in range(i + 1):
            if (j == 0) or (j == 1):
                row.append(1)
            else:
                row.append(triangle[i -1][j] + triangle[i - 1][j - 1])
        triangle.append(row)
    return triangle