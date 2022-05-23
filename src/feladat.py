import sys
from unittest.util import _MAX_LENGTH


def parkereso(fiuk, lanyok):
    if(len(fiuk) != len(lanyok)):
        return False
    result = {}
    for i in fiuk:
        for j in lanyok:
            if i[0] == j[0]:
                result[i] = j
                fiuk.remove(i)
                lanyok.remove(j)
                break
    for i in fiuk:
        for j in lanyok:
            if i[len(i)-1] == j[len(j)-1] == 'i':
                result[i] = j
                fiuk.remove(i)
                lanyok.remove(j)
                break
    minimumdiff = 100000
    for i in fiuk:
        lany = ""
        minimumdiff = 100000
        for j in lanyok:
            diff = abs(len(i) - len(j))
            if diff < minimumdiff:
                minimumdiff = diff
                lany = j
        result[i] = lany
        lanyok.remove(lany)
    return result