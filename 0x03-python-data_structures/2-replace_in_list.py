#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    function that replaces an element of a list at a specific
    position (like in C).
    """
    byte = int(len(my_list))
    if idx < 0 or idx > byte:
        return my_list
    else:
        for count in range(byte):
            if count == idx:
                my_list[count] = element

    return my_list
