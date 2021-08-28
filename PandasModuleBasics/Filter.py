#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 18:27:19 2021

@author: berkay
"""

# We use 'Top1000.csv' File

import pandas as pd

films = pd.read_csv("Top1000.csv")

# print(films["title"].head()) # or print(films.title.head())
# print(films[["title","star_rating"]].head())
# print(films[:9][["title","star_rating"]].head())

# print(films[films["star_rating"]>=8.5][["title","star_rating"]])

# print(films[(films["star_rating"]>=8.5)&(films["star_rating"]<=9)][["title","star_rating"]])

# or use query ( recommand )

print(films.query("star_rating>8.8"))
print(films.query("star_rating>8.9 & star_rating<9.7"))
print(films.query("star_rating>8.9 & star_rating<9.7")[["title","star_rating"]])

