#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return
    if idx > len(my_list):
        return
    for i in range(len(my_list)):
        if i == idx:
            my_list[i] = element
        return my_list
