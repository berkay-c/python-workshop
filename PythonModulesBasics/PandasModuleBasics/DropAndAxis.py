#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 18:58:40 2021

@author: berkay
"""
# We use 'Top1000.csv' File


import pandas as pd

film = pd.read_csv("Top1000.csv")

# axis=1 => Columns     
# axis=0 => Rows
print(film.columns)
film = film.drop("content_rating",axis=1)
print(film.columns)


# delete rows

print(film)
film = film.drop(3,axis=0)
print(film)

# multiply delete

print(film)
RowstoDrop = [0,10,15,27,41,58]
film = film.drop(RowstoDrop,axis=0)
print(film)
