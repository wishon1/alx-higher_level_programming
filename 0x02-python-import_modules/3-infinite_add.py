#!/usr/bin/python3

if __name__ == "__main__":

    from sys import argv
    byte = len(argv)
    num = 0

    if byte == 1:
        print(int(0))
    elif byte > 1:
        for count in range(1, byte):
            num = num + int(argv[count])

        print("{}".format(int(num)))
