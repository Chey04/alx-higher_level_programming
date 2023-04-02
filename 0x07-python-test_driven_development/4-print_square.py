#!/usr/bin/python3

def print_square(size):
    """
    Function to print out square of sizexsize

    Args:
    size(int): size of square

    Returns:
    square made up of # of size sizexsize
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    row = "#" * size
    for i in range(size):
        print(row)
