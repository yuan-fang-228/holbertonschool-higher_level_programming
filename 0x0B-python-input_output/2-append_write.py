#!/usr/bin/python3
"""2-append_write module"""


def append_write(filename="", text=""):
    """append a string at the end of file, return number of characters added"""
    with open(filename, "a", encoding="utf-8") as myfile:
        return myfile.write(text)
