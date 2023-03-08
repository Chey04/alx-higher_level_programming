#!/usr/bin/python3
def uppercase(str):
    lenght = len(str)
    parse = 0
    for ch in range(lenght):
        if (str[parse] <= 'A'  and str[parse] >= 'Z'):
            continue
        else:
            print("{}".format(chr(ord(str[parse]) - 32)), end="")
            parse += 1
    print()
