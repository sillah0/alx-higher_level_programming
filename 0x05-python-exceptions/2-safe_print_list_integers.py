#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    ret = 0
    try:
        for i in range(x):
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                ret += 1
    except (IndexError, ValueError):
        pass
    finally:
        print()
        return ret
