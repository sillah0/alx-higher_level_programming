#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    view_keys = list(a_dictionary.keys())
    sorted_keys = sorted(view_keys)
    for key in range(len(sorted_keys)):
        print(f"{sorted_keys[key]}: {a_dictionary[sorted_keys[key]]}")
