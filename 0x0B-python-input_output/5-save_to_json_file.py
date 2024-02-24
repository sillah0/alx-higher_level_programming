#!/usr/bin/python3
"""import json module"""


import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file - function to write an object
    to a text file using json representation
    Args:
    my_obj : object
    filename : file name
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
