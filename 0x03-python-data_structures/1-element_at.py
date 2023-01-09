#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return
    if idx > len(my_list):
        return
    for i in range(len(my_list)):
        if i == idx:
            return my_list[i]

my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
