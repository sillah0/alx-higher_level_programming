#!/usr/bin/python3
"""A simple function to check if an object is an instance
of a class"""


def is_kind_of_class(obj, a_class):
    """Returns True if object is an instance and
    false if not """

    return isinstance(obj, a_class)
