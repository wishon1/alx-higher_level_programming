#!/usr/bin/python3
"""
function that prints a matrix of integers.
"""


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        i = 1
        for index in row:
            if i == len(row):
                print("{:d}".format(index), end="")
            else:
                print("{:d} ".format(index), end="")
            i = i + 1
        print()
