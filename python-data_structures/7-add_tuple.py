#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_a = list(tuple_a)
    list_b = list(tuple_b)

    if len(list_a) < 2:
        list_a = list_a + [0] * (2 - len(list_a))
    if len(list_b) < 2:
        list_b = list_b + [0] * (2 - len(list_b))

    return ((list_a[0] + list_b[0]), (list_a[1] + list_b[1]))
