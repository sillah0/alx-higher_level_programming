#!/usr/bin/python3
"""A model containing Rectangle class"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):

    """class Square that inherits from Rectangle class"""

    def __init__(self, size):
        """
        Initializes size
        Args:
            size (int): size is private and a positive integer
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """returns area of the square"""

        return self.__size * self.__size
