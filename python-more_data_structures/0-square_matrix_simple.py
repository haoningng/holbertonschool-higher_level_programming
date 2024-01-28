#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for ele in matrix:
        new_matrix.append(list(map(lambda x: x**2, ele)))
    return new_matrix
