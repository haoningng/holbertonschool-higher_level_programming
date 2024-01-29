#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(1, x+1):
            print(my_list[i], end="")
        print()
        return i
    except IndexError:
        print()
        return i
