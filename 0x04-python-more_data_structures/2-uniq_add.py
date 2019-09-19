#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    result = 0
    for i in my_list:
        if my_list.count(i) > 1 and new_list.count(i) == 0:
            new_list.append(i)
            result += i
        elif my_list.count(i) == 1:
            new_list.append(i)
            result += i
    return result
