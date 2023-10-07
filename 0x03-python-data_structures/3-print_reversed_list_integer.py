#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    byte = int(len(my_list))
    for count in range(byte - 1, - 1, - 1):
        print("{:d}".format(my_list[count]))
