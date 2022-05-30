#!/usr/bin/python3
"""100-my_int Module"""


class MyInt(int):
    """represent a class that is a rebel"""

    def __eq__(self, other):
        """overwrite the eq function to opposite"""
        return super().__ne__(other)

    def __ne__(self, other):
        """overwrite the ne function to opposite"""
        return super().__eq__(other)
