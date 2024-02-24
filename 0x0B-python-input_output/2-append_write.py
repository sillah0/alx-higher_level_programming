#!/usr/bin/python3
""" a function that appends a string"""


def append_write(filename="", text=""):
    """append_write - append a string at the end of a text file
    Args:
    filename (str): name of text file
    text (str): text to be added to text file

    Return: number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
