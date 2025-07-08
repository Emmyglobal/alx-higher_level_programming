#!/usr/bin/python3
"""
The "1-my_list" module
"""


class MyList(list):
    """
    This class inherits from list

    @methods:
        print_sorted: prints the list in sorted form.
    """
    def print_sorted(self):
        """
        It prints the list in sorted way.
        """
        print(sorted(self))
