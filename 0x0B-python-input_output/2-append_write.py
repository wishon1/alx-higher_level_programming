#!/usr/bin/python3
"""
appends a string at the end of a text file (UTF8) and
returns the number of characters added:
"""


def append_write(filename="", text=""):
    """
        append_write: append a string to to a file
        Args:
            filename: The name of the file.
            text: the text to append
        Return: return the number of string
    """
    with open(filename, mode="a", encoding="utf-8") as file_pointer:
        num_characters = file_pointer.write(text)
    return num_characters
