#!/usr/bin/python3
"""matrix_divided is a function that divides all the elements of a matrix"""

def matrix_divided(matrix, div):
    """Returns a new matrix of the divided elements 
    and rounded to 2 decimal places
    Args:
        matrix (list): list
        div (int/float): 
        
    Return: new_matrix
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        if not all(isinstance(element, (int, float)) for row in matrix for element in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]
    return new_matrix