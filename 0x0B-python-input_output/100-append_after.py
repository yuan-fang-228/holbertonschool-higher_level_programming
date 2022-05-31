#!/usr/bin/python3
"""100-append_after Module"""


def append_after(filename="", search_string="", new_string=""):
    """insert a line of text to a file"""
    filecontent = ""
    with open(filename, "r", encoding="utf-8") as myfile:
        for line in myfile:
            filecontent += line
            if search_string in line:
                filecontent += new_string
    with open(filename, "w", encoding="utf-8") as mywritefile:
        mywritefile.write(filecontent)
