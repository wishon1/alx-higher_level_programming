#!usr/bin/python3
"""
    class Student that defines a student
"""


class Student:
    """
    class student that defines a student"""
    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ public method to retrieve a dictionary """
        return self.__dict__
