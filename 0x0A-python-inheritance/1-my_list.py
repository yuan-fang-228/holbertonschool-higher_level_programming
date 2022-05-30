#!/usr/bin/python3
"""1-my_list Module"""


class MyList(list):
    """Mylist inherits from class list"""

    def print_sorted(self):
        """print a list in ascending sort"""
        print(sorted(self))
