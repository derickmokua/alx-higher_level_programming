#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# show how to retrieve an element from a list
# -----------------------------------------------------------

def element_at(my_list, idx):
    # Check if idx is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return None
    # Return the element at idx
    return my_list[idx]
