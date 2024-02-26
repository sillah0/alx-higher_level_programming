#!/usr/bin/python3
"""this is a class Base"""


class Base:
    """class Base with a private attribute __nb_objects"""

    __nb__objects = 0

    def __init__(self, id=None):
        """initialize instance attributes
        Args:
        id (int): id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb__objects += 1
            self.id = Base.__nb__objects
