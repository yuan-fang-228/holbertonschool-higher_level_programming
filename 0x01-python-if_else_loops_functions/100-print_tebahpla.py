#!/usr/bin/python3
str = ""
for c in range(122, 97, -2):
    str = str + chr(c)
    str = str + chr(c-33)
print(str, end='')
