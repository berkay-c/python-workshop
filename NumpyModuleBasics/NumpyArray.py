#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 19:26:28 2021
@author: berkay
"""

# %% Create Numpy Array

import numpy as np

numpArray = np.array([1,5,8,4,17,18])
print(numpArray) , print(numpArray.dtype)

tempnumpyArray = np.array([[1,5],[8,44],[9,11]])
print(tempnumpyArray) , print(tempnumpyArray.dtype) , print(tempnumpyArray.ndim)

# %% ReShape

import numpy as np

numpArray = np.array([1,5,8,4,17,18])
numpArray =numpArray.reshape(3,2) # or print(numpArray.reshape(2,3))
print(numpArray) , print(numpArray.dtype)
