#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 11:50:19 2021
@author: berkay
"""
# Functions
# If we need to use a code in many places, it prevents us from writing it all over again
# def function_name (parameters)


def sayHello (name):
    print("Hello! "+ name)

sayHello("John")

# %% Default Parameter Value   
def sayHello2 (name = "Guest"):
    print("Hello! "+ name)
sayHello2()

# %% Non-essential default values ​​must be at the end
def sayHello3 (name, surname = "My Friend"):
    print("Hello !"+ name +" "+surname)
sayHello3("Peter")
sayHello3("Peter","Parker")

# %% Functions That Return Value
def rightTriangleArea (a,b):
    return a*b/2

print("Area = "+str(rightTriangleArea(6, 5)))

# %% Another way of writing functions is;
rightTriangleArea2 = lambda a,b : a*b/2
print(rightTriangleArea2(8, 6))
print(type(rightTriangleArea2))

temp=rightTriangleArea2 # We can assign function to variable
print(temp(5, 4))
