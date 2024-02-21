#!/usr/bin/python3

"""lookup - a function that checks attributes
and methods of an object
"""


def lookup(obj):
    """returns a lists of available attributes
    and methods of an object"""

    return dir(obj)
