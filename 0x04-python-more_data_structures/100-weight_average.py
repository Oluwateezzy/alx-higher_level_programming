#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    nom = sum([x[0] * x[1] for x in my_list])
    den = sum([x[1] for x in my_list])
    return nom / den
