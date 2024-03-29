#!/usr/bin/python3
"""
Defines a Rectangle class.
"""


class Rectangle:
    """Represent a rectangle.
    """
    def __init__(self, width=0, height=0,):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of rectangle.
            height (int): The height of rectangle.
        """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get and set the width of the Rectangle."""
        return(self.__width)

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """Get and set the height of the Rectangle."""
        return(self.__height)

    @height.setter
    def height(self, value):
        self.__height = value
