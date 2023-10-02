#!/usr/bin/python3
""" Module contains locked class
"""


class LockedClass:
    """prevents the user from dynamically
    creating new instance attributes
    except first_name
    """
    __slots__ = ["first_name"]

    def __init__(self, first_name):
        self.first_name = first_name
