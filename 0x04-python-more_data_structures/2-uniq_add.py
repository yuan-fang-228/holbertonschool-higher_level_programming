#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_uniq_list = set(my_list)
    result = 0
    for number in my_uniq_list:
        result = result + number
    return result
