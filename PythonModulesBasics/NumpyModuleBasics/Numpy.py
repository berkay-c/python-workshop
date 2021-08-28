#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 19:26:28 2021
@author: berkay
"""

import numpy as np

x = np.arange(20).reshape(4,5)
y = np.arange(60).reshape(5,4,3)
print(x) , print(y)
print(type(x))
print("Dimension Count = "+str(x.ndim))
print(x.shape) , print(y.shape)

