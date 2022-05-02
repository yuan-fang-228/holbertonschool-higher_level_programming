#!/usr/bin/python3
def no_c(my_string):
    my_new_string = ''
    for element in my_string:
        if element == 'C' or element == 'c':
            element = ''
        my_new_string += element
    return(my_new_string)
