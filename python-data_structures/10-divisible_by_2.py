#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list.copy()
    idx = 0
    while idx < len(my_list):
        if my_list[idx] % 2 == 0:
            new_list[idx] = True
        else:
            new_list[idx] = False
        idx = idx + 1
    return new_list
