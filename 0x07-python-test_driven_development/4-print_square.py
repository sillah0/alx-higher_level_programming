#!/usr/bin/python3

"""print_square - function to print a square with the charcter '#' """
def print_square(size):
    
    """function to print the square 
    Args:
        size (int): length of the square
        
        if size is not an int/float raise a TypeError
        
        if size is less than 0 raise a valueerror
    """
    
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for _ in range(size):
        print('#' * size)
