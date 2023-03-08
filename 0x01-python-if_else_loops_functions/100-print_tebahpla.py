#!/usr/bin/python3
for i in range(90, 64, -1):
    if i % 2 != 0:
        print("{0:c}".format(i), end="")
    else:
        print("{0:c}" .format(i + 32), end="")
