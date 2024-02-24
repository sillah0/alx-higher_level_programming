#!/usr/bin/python3
"""import json module"""


import json


def from_json_string(my_str):
    """function to return an object representation by a json string"""
    return json.loads(my_str)
