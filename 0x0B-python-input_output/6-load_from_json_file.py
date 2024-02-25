#!/usr/bin/python3
"""import json module"""


import json


def load_from_json_file(filename):
    """create a python object from json file"""
    with open(filename) as f:
        return json.load(f)
