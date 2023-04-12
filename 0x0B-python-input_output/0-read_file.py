#!/usr/bin/python3
'''function to read and print file to stdout'''


def read_file(filename=""):
    '''funtion to read and print file'''
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end='')
