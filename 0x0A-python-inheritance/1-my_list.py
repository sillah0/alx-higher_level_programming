#!/usr/bin/python3
"""A class MyList"""


class MyList(list):
    """MyList is a child class inherited from
    the list class"""

    def print_sorted(self):

        """print_sorted - is a public instance method that will print
        a list in sorted format (ascending sort)"""
        print(sorted(self))
