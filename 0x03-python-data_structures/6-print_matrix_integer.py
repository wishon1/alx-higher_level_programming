#!/usr/bin/python3
"""
function that prints a matrix of integers.
"""


def print_matrix_integer(matrix=[[]]):
    for count in matrix:
        i = 1
        for index in count:
            if i == len(count):
                print("{:d}".format(index), end="")
            else:
                print("{:d}".format(index), end="")
            i = i + 1
        print()
