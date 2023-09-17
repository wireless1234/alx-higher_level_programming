#!/usr/bin/python3
"""Module contains lookup function
"""


def lookup(obj):
    """returns the list of available attributes and methods
    Args:
        obj: An object
    Returns: attributes of object
    """
    return dir(obj)
