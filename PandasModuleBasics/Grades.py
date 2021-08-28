#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 15:33:11 2021

@author: berkay
"""

# We use 'Grades.csv' file 

import pandas as pd

grades = pd.read_csv("Grades.csv") # Same features as dataframe can be used
grades.index=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
grades.columns = ["Soyisim","İsim","SSN"
                  ,"Test1","Test2","Test3","Test4"
                  ,"Final","Sonuc"]
# print(type(grades)) ,print(grades)
# print(grades.head())  # print(grades.tail())
# print(grades.loc[8]) ,print(grades.iloc[8]) 
print(grades.İsim) 
print(grades[0:8])