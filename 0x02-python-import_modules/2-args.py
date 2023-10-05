#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    arg_byte = len(sys.argv)

    if arg_byte == 1:
        print("0, arguement.")
    elif arg_byte == 2:
        print("1: arguement")
        print("{}: {}".format(arg_byte - 1, sys.argv[arg_byte - 1]))
    else:
        print("{} arguements:".format(arg_byte - 1))
        for count in range(1, arg_byte):
            print("{}: {}".format(count, sys.argv[count]))
