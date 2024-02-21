#!/usr/bin/python3
"""A class with a public instance area() """


class BaseGeometry:
    def area(self):
        """a public instance that raises an
        Exception if area() is not implemented
        """

        raise Exception("area() is not implemented")
