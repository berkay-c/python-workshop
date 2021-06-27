#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 11:50:19 2021
@author: berkay
"""

num = 10  # integer
num2 = 10.0  # float
value = "10"  # string
id = "24234234234"

print(type(num)), print(type(num2)), print(type(value))
print(float(id)+num)
print(num+20)

firststring = "python is good"
secondstring = "PythOn iS GoOD"
if(firststring.lower() == secondstring.lower()):
    print("This Strings are same")
else:
    print("This Strings aren't same")
