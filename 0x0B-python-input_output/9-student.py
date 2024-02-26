#!/usr/bin/python3
"""A class definign Student"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        instantiation of first_name, last_name and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """method: to_json - retrieves a dict representation of
        a student instance"""
        student_dict = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }
        return student_dict
