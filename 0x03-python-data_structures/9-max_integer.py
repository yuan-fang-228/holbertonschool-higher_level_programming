#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == '':
        return 0, None
    maxnumber = my_list[0]
    for number in my_list:
        if number > maxnumber:
            maxnumber = number
    return maxnumber
