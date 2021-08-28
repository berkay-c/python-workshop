#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 14:52:39 2021

@author: berkay
"""

import pandas as pd

# %% List
data = [["Aydın", 9], ["Gümüşhane", 29], ["Denizli", 20]]
dataframe = pd.DataFrame(data, columns=["İl Adı", "Plaka Kodu"])
# print(dataframe)

#  Dictionary
data2 = {"İl Adı": ["Aydın", "Gümüşhane", "Denizli"],
         "Plaka Kodu": [9, 29, 20],
         "Vatandaş İsmi": ["Berkay", "Rakibe", "Osman"]
         }
dataframe2 = pd.DataFrame(data2, index=(1, 2, 3))
# print(dataframe2)
# print(dataframe2["Plaka Kodu"]) # Only Plate Codes Income
# del dataframe2["Vatandaş İsmi"]  # Delete 'Vatandaş İsmi' Column
# dataframe2.pop("Plaka Kodu") # Delete 'Plaka Kodu' Column
print(dataframe2), print("-----------")

print(dataframe2.loc[2])  # This is index number
print("-----------")
print(dataframe2.iloc[2])  # This is casual number

dataframe3 = dataframe2.append(dataframe)  # dataframe and dataframe2 combined
# print(dataframe3)
print(dataframe3.head())  # Shows the first 5
print(dataframe3.tail())  # Shows the first 5 from the last
