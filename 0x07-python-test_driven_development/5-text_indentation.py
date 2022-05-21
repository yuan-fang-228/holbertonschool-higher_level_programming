#!/usr/bin/python3
"""5-text_indentation Module
    Prototype: def text_indentation(text):
        print text with 2 new lines after ., ? and :
        no space at the beginning and end of each printed line
"""


def text_indentation(text):
    """a function that prints the text with 2 new lines after .?:
        text must be strings, otherwise will raise TypeError
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    new_text = text.replace(".", ".\n\n")
    new_text = new_text.replace("?", "?\n\n")
    new_text = new_text.replace(":", ":\n\n")
    new_lines = []
    for line in new_text.split("\n"):
        new_lines.append(line.strip(" "))
    print_text = "\n".join(new_lines)
    print(print_text, end="")
