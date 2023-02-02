#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    lis = my_list
    copy = []
    if idx < 0 | idx > len(my_list):
        return lis
    for i in range(len(my_list)):
        if i == idx:
            copy.append(element)
        else:
            copy.append(my_list[i])
    return copy
