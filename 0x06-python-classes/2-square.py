#!/usr/bin/python3
"""Created a class square"""


class Square:

    """this is the class"""

    def __init__(self, size=0):
        """Initialize square size to 0

        Args:
            size (int): size of the square and its intialized to 0
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
