#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    roman_dic = {
                    "I": 1, "V": 5, "X": 10, "L": 50,
                    "C": 100, "D": 500, "M": 1000
                }
    roman_string = roman_string.replace("IV", "IIII")
    roman_string = roman_string.replace("IX", "VIIII")
    roman_string = roman_string.replace("XL", "XXXX")
    roman_string = roman_string.replace("XC", "LXXXX")
    roman_string = roman_string.replace("CD", "CCCC")
    roman_string = roman_string.replace("CM", "DCCCC")
    number = 0
    for key in roman_string:
        number = number + roman_dic[key]
    return number
