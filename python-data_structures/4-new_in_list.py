#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list.copy() # shallow copy of the list
    if not (idx < 0 or idx >= len(new_list)):
        new_list[idx] = element
    return new_list
