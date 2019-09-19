#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        values = sorted(a_dictionary.values())
        res = values[-1]
        for key in a_dictionary:
            if res == a_dictionary[key]:
                return key
