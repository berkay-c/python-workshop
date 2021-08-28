#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 15:21:09 2021

@author: berkay
"""

import pandas as pd

orders = pd.read_table("Orders.tsv")
print(type(orders))
print(orders.head())
print(orders.columns)
orders.item_name = orders.item_name.str.upper()
print(orders.item_name)
print(orders.item_name.str.contains("Chicken".upper()))
orders.choice_description = orders.choice_description.str.replace('[','').str.replace(']','')
print(orders.choice_description)