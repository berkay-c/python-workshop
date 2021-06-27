#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 19:26:28 2021
@author: berkay
"""
# For Loop , Break and Continue
# Break completely ends the loop
# Continue skips the current state of the loop

countrys = ["Turkey", "China", "Russia", "England", "France"]

for country in countrys:  # Anything can be written instead of country.
    if country == "England":
        print("****End loop****")
        break
    elif country == "China":
        print("****Continue****")
        continue

    print(country+" for code = "+country[0:3])

# %% While Loop

count, result = 1, 0

while count <= 10:
    result = result+count
    count = count + 1
print(result)

# %% For Range

for num in range(50):
    print(num)  # print(mnum+1)  [1-50]
for num in range(1, 10):  # [1-9]
    print(num)
for num in range(1, 10, 2):  # prints in increments of two [1-9]
    print(num)

# %% Recap Demo 2

# User enters number
# if number = 5
# *
# **
# ***
# ****
# *****

num = int(input("How Many Stars = "))
star = ""

for x in range(1, num+1):
    star = star + "*"
    print(star)

# %% Recap Demo 3

# Finding prime numbers

num = int(input("Please Enter Number = "))
prime = True
for x in range(2, num):
    if num % x == 0:
        prime = False
        break

if prime == True:
    print("This number is Prime number")
else:
    print("This number is not Prime number")
