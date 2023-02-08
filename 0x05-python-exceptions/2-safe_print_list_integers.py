#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    error = 0
    try:
        for i in range(x):
            print("{:d}".format(my_list[i]), end="")
            count += 1
    except (ValueError, TypeError):
        count += 1
        error += 1
    count -= error
    print()
    return count
