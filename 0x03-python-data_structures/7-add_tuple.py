#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    if len_a < 2:
        if len_a is 0:
            tuple_a = (0, 0)
        else:
            tuple_a += (0,)
    if len_b < 2:
        if len_b is 0:
            tuple_b = (0, 0)
        else:
            tuple_b += (0,)
    first = tuple_a[0] + tuple_b[0]
    second = tuple_a[1] + tuple_b[1]
    new_tuple = (first, second)
    return new_tuple
