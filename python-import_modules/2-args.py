#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) == 1:
        print("0 arguments.")
    else:
        print("{} argument:".format(len(argv) - 1))
        for index in range(1, len(argv)):
            print("{}: {}".format(index, argv[index]))
            index = index + 1
