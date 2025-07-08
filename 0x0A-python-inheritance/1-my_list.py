#!/usr/bin/python3
""" class that inherits from list class """


class MyList(list):
    """ inherits from list """
    def print_sorted(self):
        print (sorted(self))
