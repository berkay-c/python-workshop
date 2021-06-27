#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 19:26:28 2021
@author: berkay
"""

# Tuple
# Elements can be changed in lists but elements can't be changed in tuple
# This Data Structure provides a performance data
# Similiar to lists
# my_Tuple = ()  Empty Tuple
# my_Tuple = (1 , 2 , ["Hello",2,3.4], ['t']) Nested Tuple

my_Tuple = (1, 3, 5, "Turkey", (2, 4, 6), [9, 8, 7])  # Five Elements
my_List = [1, 3, 5, "Turkey", [2, 4, 6], (9, 8, 7)]  # Five Elements

my_List[0] = 2
# my_Tuple [0] =2  # Tuple' object does not support item assignment

print(type(my_List)), print(type(my_Tuple))
print(my_Tuple), print(my_List)
print("my_List lenght = "+str(len(my_List))
      ), print("my_Tuple lenght = "+str(len(my_Tuple)))
print(my_List[-2]), print(my_Tuple[-2])  # Second from the right

print(my_List[1:2]), print(my_Tuple[1:2]), print("-------------")

ValueofTuple = ("China")
ValueofTuple2 = ("China",)
print(type(ValueofTuple))
print(type(ValueofTuple2))
