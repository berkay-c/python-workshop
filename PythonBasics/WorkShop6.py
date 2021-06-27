#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 19:26:28 2021
@author: berkay
"""

# Matrix Addition

x = [[1, 3, 5], [2, 4, 6], [7, 8, 9]]
y = [[3, 6, 9], [2, 5, 8], [1, 4, 7]]
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(len(x)):
    for j in range(len(y)):
        result[i][j] = x[i][j]+y[i][j]
print(result)
