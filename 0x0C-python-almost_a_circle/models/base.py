#!/usr/bin/python3
"""
    Base module managing id attribute for all future classes, incrementing
    if not provided in the constructor
"""
import json


class Base:
    """ class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """
            Constructor for the Base class.

            Parameters:
            id (int, optional): Unique identifier. If provided, assigns it
                                to the id attribute.
                                If not provided, increments __nb_objects and
                                assigns the new value to id.
            """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        " returns a Json representation of list_dictionary"
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as file_ptr:
            if list_objs is None:
                file_ptr.write("[]")
            else:
                newListDic = [index.to_dictionary() for index in list_objs]
                # Use the Base class to convert the list of dictionaries into a 
                # JSON-formatted string
            file_ptr.write(Base.to_json_string(newListDic))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """eturns an instance with all attributes already set"""
