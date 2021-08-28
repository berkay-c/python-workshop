#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 22:48:11 2021

@author: berkay
"""

import pandas as pd
import numpy as np

data = np.array(["Berkay","Kerem","Ahmet","Ayşe","Derin"])

series=pd.Series(data,index=[1,2,3,4,5])
seriesclone = pd.Series(data)
print(series) , print(seriesclone)

dataclone= {"Aydın":9,"İstanbul":34,"İzmir":35}
seriesclone2 = pd.Series(dataclone)
print(seriesclone2)
