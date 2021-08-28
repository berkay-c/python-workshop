#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 15:33:40 2021

@author: berkay
"""

import pandas as pd

data1 = {
            'id':[1,2,3,4],
            'ad':["Berkay","Rakibe","Merve","Sabri"],
            'soyad':["yıldız","yıldız","yıldız","Kaya"]
        }

data2 = {
            'id':[1,3,4,7],
            'ad':["Osman","Merve","Kerem","Mustafa"],
            'soyad':["yıldız","yıldız","yıldız","Kaya"]
        }

data1Df=pd.DataFrame(data1)
data2Df=pd.DataFrame(data2)

print(data1Df)
print(data2Df)

print(pd.merge(data1Df,data2Df,on='id',how='inner'))
print(pd.merge(data1Df,data2Df,on='id',how='left'))
print(pd.merge(data1Df,data2Df,on='id',how='right'))

print(pd.concat([data1Df,data2Df],axis=1))





