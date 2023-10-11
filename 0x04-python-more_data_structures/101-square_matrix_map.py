#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda l1: list(map(lambda x: x ** 2, l1)), matrix))
