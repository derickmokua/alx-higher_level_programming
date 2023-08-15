#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# show how to retrieve an element from a list
# -----------------------------------------------------------

def element_at(my_list, idx):
    """Retrieves an element from a list

    Args:
        my_list: a list
        idx: the index of item to retrieve

    Returns:
        item at index idx
    """

    # Check for negative and out of range index
    if idx < 0:
        return None
    if idx >= len(my_list):
        return None
    return my_list[idx]
