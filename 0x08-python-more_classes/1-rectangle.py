#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """the class created"""

    def __init__(self, width=0, height=0):

        """Initialize width and height to they are set to 0

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def height(self):

        """retrieve the height"""
        return self.__height

    @height.setter
    def height(self, value):

        """set the value and check if value is an int or
        less than 0"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):

        """retrieving the width"""
        return self.__width

    @width.setter
    def width(self, value):

        """set the value and check if value is an int or
        less than 0"""
        if not isinstance(value, int):
            raise TypeError("wisth must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
