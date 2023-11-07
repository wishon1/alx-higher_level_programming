#!/usr/bin/python3
"""
function that writes a string to a text file (UTF8) and returns the
number of characters written:
"""


def write_file(filename="", text=""):
    """
        write_file - writes a string to a text file
        Args:
            filename: The filename.
            text: The text file to be written
    """
    with open(filename, mode="w", encoding="utf-8") as file_pointer:
        num_char = file_pointer.write(text)

    return num_char
