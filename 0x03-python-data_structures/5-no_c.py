#!/usr/bin/python3
def no_c(my_string):
    z = my_string.lower()
    y = [x for x in z if x != "c"]
    output_str = ""
    for i in range(len(y)):
        output_str += y[i]
    return output_str
