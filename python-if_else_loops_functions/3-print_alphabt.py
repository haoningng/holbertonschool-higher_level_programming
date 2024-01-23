#!/usr/bin/python3
for alphabet in range(ord('a'), ord('z') + 1):
    if alphabet == ord('e') or alphabet == ord('q'):
        pass
    else:
        print("{:s}".format(chr(alphabet)), end="")
