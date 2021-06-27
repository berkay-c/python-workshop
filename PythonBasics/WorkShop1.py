#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 12:44:54 2021

@author: berkay
"""
# Swap Numbers
x = 10
y = 20
print("x= "+str(x)), print("y= "+str(y))

# Swap this numbers
temp = x
x = y
y = temp
print("x= "+str(x)), print("y= "+str(y))

# %% Another way
x = 10
y = 20
x, y = y, x
print("x= "+str(x)), print("y= "+str(y))
