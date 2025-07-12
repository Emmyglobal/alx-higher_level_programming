#!/usr/bin/python3
"""function that inserts a line of text to a file after each
    after each line containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file"""
    with open(filename, "r", encoding="utf-8") as f:
        a = f.readlines()

    my_word_list = []
    for i in a:
        my_word_list.append(i)
        
        if search_string in i:
            my_word_list.append(new_string)

    print(my_word_list)

    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(my_word_list)
