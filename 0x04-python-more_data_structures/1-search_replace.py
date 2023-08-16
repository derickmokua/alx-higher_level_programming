#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for k in range(len(my_list)):
        if my_list[k] == search:
            new_list.append(replace)
        else:
            new_list.append(my_list[k])
    return new_list
