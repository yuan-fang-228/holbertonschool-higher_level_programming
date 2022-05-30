#!/usr/bin/python3
class MyList(list):
    """Mylist inherits from class list"""

    def print_sorted(self):
        """print a list in ascending sort"""
        print(sorted(self))
