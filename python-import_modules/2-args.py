#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) == 1:
        print("0 arguments.")
    else:
        if len(argv) == 2:
            print("{} argument:".format(1))
        else:
            print("{} arguments:".format(len(argv) - 1))
        for index in range(1, len(argv)):
            print("{}: {}".format(index, argv[index]))
            index = index + 1
