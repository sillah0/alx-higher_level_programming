#!/usr/bin/python3
"""a simple function to check if object is
an instance of a specified class"""


def is_same_class(obj, a_class):

    """Returns True if object ia an instance and
    false if not """
    return type(obj) is a_class
