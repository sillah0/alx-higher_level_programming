#!/usr/bin/python3
"""A simple function if an object is an instance
of a class that it inherited"""


def inherits_from(obj, a_class):

    """check if the object is an instance of a class that inherited
    (directly or indirectly)"""

    return type(obj) is not a_class and issubclass(type(obj), a_class)
