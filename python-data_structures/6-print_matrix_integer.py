#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("")
    else:
        for ele in matrix:
            for integer in ele:
                if (integer != ele[len(ele) - 1]):
                    print("{:d}".format(integer), end=" ")
                else:
                    print("{:d}".format(integer))
