#!/usr/bin/python3
"""this is a class Base"""
import json

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

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
