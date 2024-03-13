#!/usr/bin/python3
def remove_char_at(string, n):
    newStr = ''
    i = 0
    for c in string:
        if i != n:
            newStr += string[i]
        i += 1
    return newStr
