#!/usr/bin/python3
"""Created a class square"""


class Square:
    """This is the class square created"""

    def __init__(self, size=0):
        """Initialize square size

        Args:
            size (int): size of square initialized to 0
        """
        self.size = size

    @property
    def size(self):
        """the getter method retrives the value of the
        private attribute size and returns its value"""
        return self.__size

    @size.setter
    def size(self, value):
        """the setter method does check the value returned by the getter
        method if its an integer and if the value is greater than 0
        returning two specified error and setting the given value"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """calculate the area"""
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(1, self.size + 1):
                print("#" * self.size)
