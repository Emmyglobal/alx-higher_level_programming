#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dict_keys = []
    for k, v in a_dictionary.items():
        if v == value:
            dict_keys.append(k)
    for i in dict_keys:
        del a_dictionary[i]
    return a_dictionary
