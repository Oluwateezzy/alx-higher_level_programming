#!/usr/bin/python3
def uniq_add(my_list=[]):
    copy = []

    for i in my_list:
        if i not in copy:
            copy.append(i)

    return sum(copy)
