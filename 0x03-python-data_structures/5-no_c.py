#!/usr/bin/python3
def no_c(my_string):
    strcpy = []
    for i in range(len(my_string)):
        if my_string[i] == 'c' or my_string[i] == 'C':
            continue
        strcpy.append(my_string[i])
    new_string = ''.join(strcpy)
    return new_string
# return my_string.translate({ord(c): None for c in "cC"})
