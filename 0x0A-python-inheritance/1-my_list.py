#!/usr/bin/python3
'''Defines an inherited list class.'''


class MyList(list):
    '''Sort and print a list in ascending order'''

    def print_sorted(self):
        '''Print a list in sorted ascending order.'''
        print(sorted(self))
