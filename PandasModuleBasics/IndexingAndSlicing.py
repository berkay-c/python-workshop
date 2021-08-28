#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 15:55:31 2021

@author: berkay
"""

import pandas as pd

grades = pd.read_csv("Grades.csv")

grades.columns=["Soyisim","İsim","SSN"
                ,"Test1","Test2","Test3","Test4"
                ,"Final","Sonuç"]

print(grades.loc[:,"İsim"])
print(grades.loc[:5,"İsim"])
print(grades.loc[:5,"İsim":"Test4"])
print(grades.loc[:5,["İsim","Final","Sonuç"]]) , print("--------------------")
print(grades.loc[::-1,"Soyisim"])