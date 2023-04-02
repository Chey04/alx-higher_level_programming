#!/usr/bin/python3

def add_integer(a, b=98):
    """
    This function takes two args and returns their sum

    Args:
    a (int): arg 1
    b (int): arg 2

    Return:
    The sum of a and b
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b ,(int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
