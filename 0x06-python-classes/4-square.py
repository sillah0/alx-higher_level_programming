#!/usr/bin/python3

"""create a class square"""


class Square:

    """this is the class created"""
    def __init__(self, size=0):

        """Initialize size of square"""

        self.size = size

        """@property is a decorator to define
        getter method for class property"""
    @property
    def size(self):
        """size property is defined
        this size getter method is for retriving the
        value of __size which is a private attribute """
        return self.__size

    """the setter checks if the int retrived by size getter method
    is an int or less than 0"""

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size mut be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size * self.__size
