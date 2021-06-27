#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 19:26:28 2021
@author: berkay
"""
# Factorial Calculation Using Functions

def factorialCalc(num):
    if num == 0:
        return 1
    else:
        return num*factorialCalc(num-1)

number = int(input("Please Enter Number : "))
if number < 0:
    print("I can't calculate this number because it's negative number ")
else:
    print(factorialCalc(number))
