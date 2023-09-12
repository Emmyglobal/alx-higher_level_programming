#!/usr/bin/python3
"""Class Mylist that inherits from list"""


class MyList(list):
    """Mylist that inherits from list"""
    def print_sorted(self):
        print(sorted(self))
