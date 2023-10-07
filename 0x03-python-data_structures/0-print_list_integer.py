#!/usr/bin/python3
def print_list_integer(my_list=[]):
    str_len = len(my_list)
    for count in range(str_len):
        print("{:d}".format(my_list[count]))
