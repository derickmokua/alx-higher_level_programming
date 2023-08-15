#!/usr/bin/python3

# -----------------------------------------------------------
# Python program that:
# demonstrates how to print all integers of a list, in reverse order
# -----------------------------------------------------------

def print_reversed_list_integer(my_list=[]):
    """prints integers of a list in reverse order

    Args:
        my_list:a list
    """
     if my_list:
        my_list.reverse()
        for item in my_list:
            print("{:d}".format(item))
