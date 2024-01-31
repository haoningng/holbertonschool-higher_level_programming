#!/usr/bin/python3
"""
Module: 2-matrix_divided.py

Function: matrix_divided()
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix

    Args:
    matrix: list of lists of integers or floats
    div(int/float): number by which each elements of matrix is divided

    Return:
    A new matrix
    """
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for list in matrix:
        length = 0
        new_list = []
        for ele in list:
            length += 1
            if not (isinstance(ele, int) or isinstance(ele, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers"
                    "/floats"
                    )
            new_list.append(round(ele / div, 2))
        if length != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        new_matrix.append(new_list)
    return new_matrix
