#!/usr/bin/python3
"""a function that writes a string to a text file"""


def write_file(filename="", text=""):
    """write_file - writes a string to a text file

    Args:
    filename (str): name of the text file
    text (str): string to be written in text file

    Returns: number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
