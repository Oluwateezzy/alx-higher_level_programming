#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    lis = my_list
    if idx < 0 || idx > len(my_list):
        return lis
    for i in range(len(my_list)):
        if i == idx:
            lis[i] = element
    return lis
