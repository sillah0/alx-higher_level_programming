#!/usr/bin/python3

"""Create a class square"""


class Square:
    """this is the class created"""

    def __init__(self, size=0):

        """Initialize the size of the square to 0

        Args:
            size (int): size of the square
            """
        self.__size = size

        """The if statements are checking if size is of integer type
        and if it's not an int returns a TypeError of a specified message
        and checks again if size is less than 0 and
        returns a ValueError of a specified message
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """A method to calculate the area of a square
        and return the area"""
        return self.__size * self.__size
