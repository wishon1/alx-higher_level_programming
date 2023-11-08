#!/usr/bin/python3
""" class Student that defines a student by:
    (based on 9-student.py)
"""


class Student:
    """ Student class """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the student class """

        if (type(attrs) is list and
                all(type(elem) is str for elem in attrs)):
            return {e: getattr(self, e) for e in attrs if hasattr(self, e)}
        return self.__dict__

    def reload_from_json(self, json):
        """ replaces all attributes of the Student instance """
        for e, value in json.items():
            setattr(self, e, value)
