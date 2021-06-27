#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 19:26:28 2021
@author: berkay
"""

# Lists, tuples, dictionaries, and sets are all iterable objects.
# It allows us to traverse the elements of the above objects.

countryList = ["Turkey","France","Usa","England"] 

iterators = iter(countryList)

print(next(iterators))
print(next(iterators))
print(next(iterators))
print(next(iterators))

