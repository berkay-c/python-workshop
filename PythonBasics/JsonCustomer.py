#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 19:26:28 2021
@author: berkay
"""

import json

with open("Customers.json") as users:
    data = json.load(users)
    print(data), print("--------")
    
    for i in range(5):
        print(data[i]["username"])
        print(data[i]["email"])
        #print(data[i]["address"]), print("--------")
        #print(data[i]["address"]["street"])
        #print(data[i]["address"]["geo"]["lat"])
        print(data[i]["company"]["name"]), print("--------")