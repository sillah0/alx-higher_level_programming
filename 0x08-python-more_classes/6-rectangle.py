#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """the class created"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):

        """Initialize width and height to they are set to 0

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        for i in range(self.__height):
            rectangle_str += "#" * self.__width
            if i != self.__height - 1:
                rectangle_str += "\n"
        return rectangle_str

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
