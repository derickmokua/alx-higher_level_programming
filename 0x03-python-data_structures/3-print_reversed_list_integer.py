#!/usr/bin/python3

# -----------------------------------------------------------
# Python program that:
# demonstrates how to print all integers of a list, in reverse order
# ----------------------------------------------------------
def print_reversed_list_integer(my_list=[]):
    # Reverse the list
    reversed_list = my_list[::-1]

    # Iterate over the reversed list
    for num in reversed_list:
        # Use str.format() to print each integer
        print("{:d}".format(num))
