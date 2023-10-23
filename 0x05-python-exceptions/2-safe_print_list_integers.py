#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    function that prints the first x elements of a list and only integers.
    """
    count = 0
    for num in range(x):
        try:
            if type(my_list[num] == int):
                print("{:d}".format(my_list[num]), end="")
                count += 1
        except (ValueError, TypeError):
            pass
    print()
    return count
