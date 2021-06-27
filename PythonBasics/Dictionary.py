#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 19:26:28 2021
@author: berkay
"""

# Dictionary
# Holds unordered data like a set
# my_dict = {1 : 'apple' , 2 : 'carrot'}

my_dictionary = {
    "book": "kitap",
    "table": "masa",
    "door": "kapı"
}
my_dictionary2 = dict(kitap="book", masa="table")

print(my_dictionary), print("-------"), print(my_dictionary["door"])
my_dictionary["pencil"] = "kalem"
print("-------"), print(my_dictionary)
del(my_dictionary["table"])
print("-------"), print(my_dictionary), print(len(my_dictionary))
