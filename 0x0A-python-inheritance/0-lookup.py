#!/usr/bin/python3

def lookup(obj):
    result = []
    for attribute in dir(obj):
        result.append(attribute)
    return result
