#!/usr/bin/python3
"""This file contains the function for evaluating the Pascal's triangle."""


def pascal_triangle(n):
    """This function returns a list of lists representing Pascal's
    triangle of n rows.
    
    Parameters:
    n: An integer representing the number of rows in the Pascal's
    triangle.
    
    Returns:
    A list of lists representing Pascal's triangle. Returns an empty
    list if n <= 0.
    """
    if n <= 0:
        return []
    
    triangle = [[1]]
    if n > 1:
        triangle.append([1, 1])
    
    # Building the triangle row by row
    for i in range(2, n):
        p = triangle[i-1]
        current_row = [sum(pair) for pair in zip([0] + p, p + [0])]
        triangle.append(current_row)

    return triangle