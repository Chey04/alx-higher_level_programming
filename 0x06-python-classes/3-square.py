#!/usr/bin/python3
"""Defining a class: Square"""


class Square:
    """created a class called square"""

    def __init__(self, size=0):
        """initializing some attributes

        Args:
            size (int): size of square
        """

        if not type(size) is int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self._Square__size = size

    def area(self):
        """method to find area of square"""

        self_area = self._Square__size ** 2
        return (self_area)
