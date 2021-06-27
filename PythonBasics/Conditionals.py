#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 19:26:28 2021
@author: berkay
"""
# %% if ,elif ,else

num1, num2 = 20, 30
if num1 < num2:
    print("A")
    print("B")
print("C"), print("----------")

# %% Recap Demo 1
# Traffic Lights
lights = ["red", "yellow", "green"]
currentlights = lights[int(input("{Red (1) , Yellow (2) , Green(3)} Choose One = "))-1]

if currentlights == "red":
    print("STOP")
elif currentlights == "yellow":
    print("GET READY")
else:
    print("PASS")
