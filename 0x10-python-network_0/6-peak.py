#!/usr/bin/python3
""" a function that finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ This function returns the peak of the list """
    if (len(list_of_integers) == 0):
        return None

    else:
        top = list_of_integers[0]
        for i in range(len(list_of_integers)):
            if list_of_integers[i] > top:
                top = list_of_integers[i]
        return top