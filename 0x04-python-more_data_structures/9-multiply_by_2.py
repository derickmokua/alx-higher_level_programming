#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_d = {}
    for k in a_dictionary:
        new_d[k] = a_dictionary[k] * 2
    return new_d
