#!/usr/bin/python3
"""
Module contains the Student class
"""


class Student:
    """
    Defines a Student with firstname, Lastname and Age
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialize firstname lastname and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        get dictionary representation of object
        Args:
            attrs: Attributes to filter
        Return:
            Dictionary representation of object
        """
        new_dict = {}
        if type(attrs) is list:
            for i in attrs:
                if i in self.__dict__:
                    new_dict[i] = self.__dict__[i]
        return new_dict
