#!/usr/bin/python3
if __name__ == "__main__":

    from sys import argv

    arg_byte = len(sys.argv)

    if arg_byte == 1:
        print("0, arguement.")
    else:
        if arg_byte == 2:
            print("{} arguement:".format(arg_byte - 1))
        else:
            print("{} arguements:".format(arg_byte - 1))
        for count in range(1, arg_byte):
            print("{}: {}".format(count, sys.argv[count]))
