#!/usr/bin/python3

"""
Retrieves an element from a Python list, mimicking C-style list indexing.

Parameters:
    my_list (list): The list from which to retrieve the element.
    idx (int): The index of the element to retrieve.

Returns:
    The element located at the specified index within the list.
"""

#Validate for negative and out-of-range indices.

if idx < 0:
        return None
    if idx >= len(my_list):
        return None
    return my_list[idx]
