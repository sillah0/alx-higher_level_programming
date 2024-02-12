#!/usr/bin/python3
""" add_integer is a function that takes two arguments a & b
checks if a & b are of type int or float then
typecast float to int a=int(a)
raise TypeError: a / b must be integers
"""

def add_integer(a, b=98):
    """adds two integers a & b
    returns the addition result
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must ba an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    a = int(a)
    b = int(b)

    return a + b
