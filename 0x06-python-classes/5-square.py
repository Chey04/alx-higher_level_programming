#!/usr/bin/python3
"""Defining a class: Square"""


class Square:
    """created a class called square"""

    def __init__(self, size=0):
        """initializing some attributes

        Args:
            size (int): size of square
        """

        self.size = size

    @property
    def size(self):
        """get and set current size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not type(value) is int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """area of square"""

        self_area = self._Square__size ** 2
        return self_area

     def my_print(self):
        """Print the square with the # character."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
