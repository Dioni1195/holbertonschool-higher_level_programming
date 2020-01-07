#!/usr/bin/python3
""" This module has the function find_peak """


def find_peak(list_of_integers):
    """ This function finds the peak of a list
        Args:
        list_of_integers(list): List of numbers
    """
    if len(list_of_integers) == 0:
        return None

    mid = int(len(list_of_integers)/2)
    if mid + 1 < len(list_of_integers):
        right = list_of_integers[mid + 1]
        if list_of_integers[mid] < right:
            return find_peak(list_of_integers[mid + 1:])
        else:
            return find_peak(list_of_integers[:mid + 1])
    elif mid - 1 >= 0:
        left = list_of_integers[mid - 1]
        if list_of_integers[mid] > left:
            return list_of_integers[mid]
        else:
            return find_peak(list_of_integers[:mid])
    return list_of_integers[mid]
