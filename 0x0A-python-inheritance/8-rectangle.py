#!/usr/bin/python3
""" Module defines rectangle class
"""


class Rectangle(BaseGeometry):
    """Rectangle class definition
    """

    def __init__(self, width, height):
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
