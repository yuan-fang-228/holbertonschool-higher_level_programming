#!/usr/bin/python3
"""1-write_file module"""


def write_file(filename="", text=""):
    """write a string to a text file and return number of character written"""
    with open(filename, "w", encoding="utf-8") as myfile:
        return myfile.write(text)
