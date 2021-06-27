#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 19:26:28 2021
@author: berkay
"""
# Map , Filter , Reduce

def calculateSquare(n):
    return n*n

def mapfiltreted(x):
    return x>2

numbers = (1, 2, 3, 4)
result = set(map(calculateSquare, numbers))
result2 = set(filter(mapfiltreted, numbers))
print(result)
print(result2)

from functools import reduce
factorial = reduce(lambda x,y : x*y,  numbers)

print(factorial)
 