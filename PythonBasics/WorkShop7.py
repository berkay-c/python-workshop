#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 19:26:28 2021
@author: berkay
"""

# Word Sorting

sentence = str(input("Please Enter Sentence = "))
sentencesplit = sentence.split()
sentencesplit.sort()

for word in sentencesplit:
    print(word)