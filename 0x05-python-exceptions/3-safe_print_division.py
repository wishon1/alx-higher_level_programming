#!usr/bin/python3
def safe_print_division(a, b):
    """ divides 2 integers and prints the result."""
    try:
        result_div = a / b
    except (TypeError, ZeroDivisionError):
        result_div = None
        return result_div
    finally:
        print("Inside result: {}".format(result_div))

        return result_div
