#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        for i in range(x):
            if type(my_list[i]) not int:
                pass
            print("{:d}".format(my_list[i]), end="")
    except ValueError:
        print()
        return i
    except TypeError:
        print()
        return i
    print()
    return x
