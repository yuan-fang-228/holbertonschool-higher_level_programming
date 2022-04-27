#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i, 10):
        if i < j:
            print(i, end='')
            if i == 8 and j == 9:
                print(j)
            else:
                print(j, end=', ')
