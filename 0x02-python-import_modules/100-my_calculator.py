#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import sub, add, mul, div
    from sys import argv, exit

    _len = len(argv)

    if _len > 4 or _len < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        n = [None] * 4
        for count in range(1, _len):
            n[count] = argv[count]

        if n[2] == "+":
            print("{} + {} = {}".format(n[1], n[3], add(int(n[1]), int(n[3]))))
        elif n[2] == "-":
            print("{} - {} = {}".format(n[1], n[3], sub(int(n[1]), int(n[3]))))
        elif n[2] == "*":
            print("{} * {} = {}".format(n[1], n[3], mul(int(n[1]), int(n[3]))))
        elif n[2] == "/":
            print("{} / {} = {}".format(n[1], n[3], div(int(n[1]), int(n[3]))))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
