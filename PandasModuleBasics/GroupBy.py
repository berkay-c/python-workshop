#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 18:27:19 2021

@author: berkay
"""

# We use 'Top1000.csv' File

import pandas as pd

film = pd.read_csv("Top1000.csv")

print(film.columns)
print(film.star_rating.mean())
print(film.groupby("genre").star_rating.mean()) 