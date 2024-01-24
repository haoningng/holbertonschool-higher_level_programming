#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for ele in matrix:
        for integer in ele:
            if (integer != ele[len(ele) - 1]):
                print("{}".format(integer), end=", ")
            else:
                print("{}".format(integer))
