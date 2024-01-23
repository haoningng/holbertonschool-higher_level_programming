#!/usr/bin/python3
for i in range(0, 10):
    print("{:02}".format(i), end=", ")
for i in range(10, 100):
    if str(i)[0] != str(i)[1] and str(i)[0] < str(i)[1]:
        if i != 89:
            print("{:02}".format(i), end=", ")
        else:
            print("{:02}".format(i))
