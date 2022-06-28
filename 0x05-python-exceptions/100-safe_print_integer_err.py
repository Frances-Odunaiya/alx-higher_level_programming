#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    is_int = True
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as err:
        is_int = False
        print(f"Exception: {err}", file=sys.stderr)
    return is_int
