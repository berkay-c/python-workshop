#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 19:19:26 2021

@author: berkay
"""

import pandas as pd

data = pd.read_csv("http://bit.ly/uforeports")

print(data.columns)

print(data.isnull().head(10))
print(data.isnull().sum())
print(data[data.City.isnull()])

print(data.shape)
# data=data.dropna(how = "all")
# data = data.dropna(subset = ["City","Colors Reported"],how = "any")

data["Shape Reported"].fillna(value="Belirsiz ", inplace=True)
print(data["Shape Reported"].value_counts(dropna=False))
print(data.shape)
