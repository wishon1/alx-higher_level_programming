#!/usr/bin/python3
""" peak sorking algorithm """


def find_peak(list_of_integers):
    """ find the peak number in the list """
    if not list_of_integers:
        return None

    num = 0
    for index in range(len(list_of_integers)):
        if (list_of_integers[index - 1] is None or list_of_integers[
                index] > list_of_integers[index - 1]):
            if (index + 1 == len(list_of_integers) or list_of_integers[
                    index] > list_of_integers[index + 1]):
                num = list_of_integers[index]
                break
    if num == 0:
        num = list_of_integers[index]

    return num
