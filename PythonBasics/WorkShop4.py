#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 19:26:28 2021
@author: berkay
"""

# User enters three integers
# Prints the largest of the entered numbers to the screen.

num1 = int(input("First number = "))
num2 = int(input("Second number = "))
num3 = int(input("Third number = "))
my_list = []
my_list.append(num1), my_list.append(num2), my_list.append(num3)
my_list.sort()
print("\n"+str(my_list[2]))

# %% or

if num1 > num2 and num1 > num3:
    largestnumber = num1
elif num2 > num1 and num2 > num3:
    largestnumber = num2
else:
    largestnumber = num3
    
print("\n"+str(largestnumber))
