#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 19:26:28 2021
@author: berkay
"""

# Working With Json Data

import json
data = '{"firstName":"Peter","lastName":"Parker" }' # This is Json Format

temp = json.loads(data)

print(type(temp))
print(temp["firstName"])
print(temp["lastName"])

Customer = {
    "firstName" :"Berkay",
    "eMail":"c.berkay@outlook.com"
    }

# Dumps are used when python objects are translated
CustomerJson = json.dumps(Customer)
print(Customer) # Converted to Json Format
