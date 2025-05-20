#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    r_list = my_list.copy()
    if idx < 0 or idx > len(r_list):
        return (my_list)
    else:
        r_list[idx] = element
        return (r_list)
