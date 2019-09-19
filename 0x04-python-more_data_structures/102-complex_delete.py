#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_del = []
    for val_del in a_dictionary:
        if a_dictionary[val_del] == value:
            list_del.append(val_del)
    for key_del in list_del:
        del a_dictionary[key_del]
    return a_dictionary
