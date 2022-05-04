#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    score = 0
    weight = 0
    for element in my_list:
        score = score + element[0] * element[1]
        weight = weight + element[1]
    return (score / weight)
