#!/usr/bin/python3
"""
Module defines rectangle class
rectangle class inherits base geometry
"""


class Rectangle(BaseGeometry):
    """Rectangle class definition
    Rectangle inherits base geometry
    """

    def __init__(self, width, height):
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
