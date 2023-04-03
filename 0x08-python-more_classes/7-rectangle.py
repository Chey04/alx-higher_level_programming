#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle.
    Attributes:
        number_of_instances (int): The number of Rectangle instances.
        print_symbol (any): The symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Return the area of the Rectangle."""
        return(self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 and self.__height == 0:
            return(0)
        return(2 * (self.__width + self.__height))

    def __str__(self):
        """Return the printable representation of the Rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return('')
        rec_str = ''
        symbol = str(self.print_symbol)
        for i in range(self.__height):
            rec_str = rec_str + symbol * self.__width
            if i != self.__height - 1:
                rec_str += '\n'
        return (rec_str)

    def __repr__(self):
        """Returns exact  string representation of the Rectangle."""
        return("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """Print a message and decrease count for every deletion of a Rectangle."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

