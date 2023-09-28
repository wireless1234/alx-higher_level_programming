#!/usr/bin/python3
"""
This module contains the Rectangle Class
"""


class Rectangle:
    """
    A Rectangle class.
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        mystr = ""
        if self.__height == 0 or self.__width == 0:
            return mystr
        for i in range(self.__height):
            mystr += '#' * self.__width
            if i is not self.__height - 1:
                mystr += '\n'
        return mystr

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
    @staticmethod
    def __del__():
        print("Bye rectangle...")
