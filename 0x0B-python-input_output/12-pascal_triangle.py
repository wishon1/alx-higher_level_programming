#!/usr/bin/python3
""" This module supplies two functions,
calculate_pascal_triangle and generate_next_row to return
a list of lists of integers representing the
Pascal’s triangle of n"""


def pascal_triangle(n):
    """ Calculate Pascal's triangle for a given number of rows """
    triangle_matrix = []
    for current_row in range(n):
        if current_row == 0:
            row = [1]
            triangle_matrix.append(row)
        else:
            """ Generate a new row list based on the previous list """
            row = generate_next_row(row)
            triangle_matrix.append(row)
    return triangle_matrix


def generate_next_row(previous_row):
    """ Generates the next row based on the previous row """
    new_row_length = len(previous_row) + 1
    new_row = [0] * new_row_length
    for i in range(new_row_length):
        if i == 0 or i == new_row_length - 1:
            """ The first and last index must be 1"""
            new_row[i] = 1
        else:
            new_row[i] = previous_row[i - 1] + previous_row[i]
    return new_row
