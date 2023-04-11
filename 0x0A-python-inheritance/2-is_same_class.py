#!/usr/bin/python3
'''Defines a method that checks if the object is a class instance.'''


def is_same_class(obj, a_class):
    '''Checks whether an object is instance or not from a given class.

    Args:
        obj (any): The object to check.
        a_class (type): Object to chack against.
    Return:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    '''
    if type(obj) == a_class:
        return True
    return False
