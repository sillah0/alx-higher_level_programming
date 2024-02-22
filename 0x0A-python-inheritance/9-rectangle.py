#!/usr.bin/python3
"""A module that contains a rectangle class"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """A class inherited from BaseGeometry"""

    def __init__(self, width, height):
        """
        instantiation of the width and height
         Args:
         width (int): must be private and a paositive integer validated by
                        integer_validator
         height (int): must be private and a paositive integer validated by
                        integer_validator
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of a rectangle"""
        return self.__height * self.__width

    def __str__(self):
        """return the following ractangle description
        [Rectangle] <width>/<height>
        """
        return "[Rectangle] {:d}/{:d}".format(self.__height, self.__width)
