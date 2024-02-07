#!/usr/bin/python3
"""This module defines the pascal_triangle function"""


def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascal’s
    triangle of n

    Args:
    n: height of the Pascal's triangle
    """
    if n <= 0:
        return []
    list = [[1]]
    for i in range(1, n):
        inner_list = [1]
        for j in range(1, i):
            inner_list.append(list[i - 1][j - 1] + list[i - 1][j])
        inner_list.append(1)
        list.append(inner_list)
    return list
