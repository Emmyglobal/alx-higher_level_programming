#!/usr/bin/python3
# A Function that deletes keys with a specific value in a dictionary.

def complex_delete(a_dictionary, value):
    while value in a_dictionary.values():
        for k, v in a_dictionary.items():
            if v == value:
                del a_dictionary[k]
                break

    return (a_dictionary)
