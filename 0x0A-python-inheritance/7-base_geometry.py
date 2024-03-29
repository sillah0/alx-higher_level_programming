#!/usr/bin/python3
"""class BaseGeometry"""


class BaseGeometry:

    """
    a public attribute area
    """

    def area(self):
        """a public instance that raises an
        Exception if area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Method: integer_validator - validates a integer
        Args:
        name (str) - name of value
        value (int) - integer
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greator than 0".format(name))
