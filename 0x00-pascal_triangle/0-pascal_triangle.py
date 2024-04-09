#!/usr/bin/python3
"""_summary_"""

def pascal_triangle(n):
    """This function returns a list of lists representing Pascal's triangle of n rows.
    
    Args:
    n: An integer representing the number of rows in the Pascal's triangle.
    
    Returns:
    A list of lists representing Pascal's triangle. Returns an empty list if n <= 0.
    """
    
    if n <= 0:
        return []
    
    # Base case; first row is always [1]
    triangle = [[1]]
    
    # Building the triangle row by row
    for i in range(1, n):
        previous_row = triangle[i-1]
        current_row = triangle[1]
        for j in range(1, i):
            current_row.append(previous_row[j-1] + previous_row[j])
        # End each row with 1
        current_row.append(1)
        triangle.append(current_row)
        
    return triangle