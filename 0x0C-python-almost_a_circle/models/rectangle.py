#!/usr/bin/python3
"""Import superclass Base"""


from models.base import Base


class Rectangle(Base):
    """class Rectangle inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializing instance atrributes
        Args:
        width (int): width
        height (int): height
        x (int): x
        y (int): y
        id (int): id
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """get witdh
        Return : width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """set width
        Args:
        value (int): value
        Return: width
        """
        self.__width = value

    @property
    def height(self):
        """get height
        Return : height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """set height
        Args:
        value (int): value
        Return: height
        """
        self.__height = value

    @property
    def x(self):
        """get x
        Return : x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """set x
        Args:
        value (int): value
        Return: x
        """
        self.__x = value

    @property
    def y(self):
        """get y
        Return : y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """set y
        Args:
        value (int): value
        Return: y
        """
        self.__y = value
