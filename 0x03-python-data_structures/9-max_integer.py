#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    max = my_list[0]
    for i in range(len(my_list)):
            if i is not len(my_list) - 1:
                if my_list[i] > my_list[i + 1] and my_list[i] > max:
                    max = my_list[i]
            elif i is len(my_list) - 1 and my_list[i] > max:
                max = my_list[i]
    return max
