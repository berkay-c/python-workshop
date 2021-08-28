#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 19:26:28 2021
@author: berkay
"""

# Basics Operations

import numpy as np
temp = np.array([20, 30, 40, 50])
temp2 = np.arange(4)  # 0 , 1 , 2 , 3

c = temp-temp2
d = temp2**2
print(temp), print(temp2), print(c), print(d), print(d < 8)
print(temp * temp2)  # ElementWise Product
print(temp@temp2)  # or print(temp.dot(temp2))

# %% Create  one and zero matrix
a = np.ones((3, 4))
b = np.zeros((7, 5))
c = np.random.random((3, 4))
d = np.sum(a)  # sum all numbers
e = np.array([2, 3, 4, 5])
k = np.sqrt(e)
print(a), print(b), print(c), print(d), print(
    e.min()), print(e.max()), print(k)
