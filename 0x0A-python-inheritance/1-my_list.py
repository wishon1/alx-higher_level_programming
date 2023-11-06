#!/usr/bin/pyhton3
""" class MyList that inherits from list """


class MyList(list):
    """
        Mylist - class that prints a sorted list.
        list: list to print out.
        Return: Return the sorted list.
    """
    def print_sorted(self):
        """ function to print the sorted list """
        new_list = sorted(self)
        print(new_list)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
