def search_replace(input_list, search, replace):
    new_list = []
    for element in input_list:
        if element == search:
            new_list.append(replace)
        else:
            new_list.append(element)
    return new_list

