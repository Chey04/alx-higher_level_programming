#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    Only attributes named 'first_name' can be created.
    """

    __slots__ = ["first_name"]
