#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    arg_byte = len(argv) - 1
    arg_str = "argument" if arg_byte == 1 else "arguments"
    delim = "." if arg_byte == 0 else ":"

    print("{} {}{}".format(arg_byte, arg_str, delim))

    for count in range(1, arg_byte + 1):
        print("{}: {}".format(count, argv[count]))
