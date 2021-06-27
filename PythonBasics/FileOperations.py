#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 19:26:28 2021
@author: berkay
"""

# Reading a File
# r Read 
# a Append 
# w Write
# x creat

file = open("Customer.txt")  # File Creation

# print(file.read())  # File Read # Reading All Line
# print(file.read(5)) # Read First 12 Character 
# print(file.readline())  # Berkay Çiftçi  # Reading Line By Line
# print(file.readline())  # Derin Yılmaz   # Reading Line By Line

for read in file:
    print(read)
    
file.close()

# %% File Write 

filetoAppend = open("Students.txt","w")
filetoAppend.write("Asli Demir \n")
filetoAppend.write("John Parker \nPeter Parker")
filetoAppend.close()

# %% File Delete 

import os 
if os.path.exists("Students.txt"):
    os.remove("Students.txt")
else:
        print("This File absent")
        
# %% Folder Remove
# Create "Empty" Folder

import os  
os.rmdir("Empty")  # Deletes Wallpaper Folder

# %% Recap Demo 4

Students = ["Berkay","Kerem","Derin","Asli"]

AppendFile = open("RecapDemoStudents.txt","a")

for student in Students:
    AppendFile.write(student)
    AppendFile.write("\n")

AppendFile.close()














