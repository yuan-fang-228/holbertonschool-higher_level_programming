#!/usr/bin/python3
"""0-read_file Module"""


def read_file(filename=""):
    """a function that read a text file and print it to stdout"""

    with open(filename, encoding='utf-8') as myfile:
        print(myfile.read(), end='')
