#!/usr/bin/pyhton3
"""
     function that reads a text file (UTF8) and prints it to stdout:
"""


def read_file(filename=""):
    """ function that prints the result of a text file """
    with open(filename, mode="r", encoding="utf-8") as file_pointer:
        print(file_pointer.read(), end="")
