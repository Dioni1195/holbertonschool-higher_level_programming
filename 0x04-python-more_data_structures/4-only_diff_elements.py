#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    if (len(set_1) != 0 and len(set_2) != 0) and (set_1 is not None and set_2 is not None):
        return set_1 ^ set_2
    else:
        return {}
