#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 19:26:28 2021
@author: berkay
"""

# Basics Calculator


def Addition(num1, num2):
    return num1+num2


def Subtraction(num1, num2):
    return num1-num2


def Multiplication(num1, num2):
    return num1*num2


def Division(num1, num2):
    return num1/num2


numberone = int(input("Please Enter Number One : "))
numbertwo = int(input("Please Enter Number Two : "))

selection = int(input(" 1-Addition process \n 2-Subtraction \n 3-Multiplication \n 4-Division process \n Which one do you choose = "))


if selection == 1:
    print("\nResult : "+str(Addition(numberone, numbertwo)))
elif selection == 2:
    print("\nResult : "+str(Subtraction(numberone, numbertwo)))
elif selection == 3:
    print("\nResult : "+str(Multiplication(numberone, numbertwo)))
elif selection == 4:
    print("\nResult : "+str(Division(numberone, numbertwo)))
else:
    print("\nSomething Gone Wrong")
