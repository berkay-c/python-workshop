#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 19:26:28 2021
@author: berkay
"""

# Set
# Similiar to lists
# No index and no queue
# No data duplication
# This Data Structure provides a performance data
# All elements unique
# my_Set = {1,2,3,4,5,6} set of integers
# my_Set = {1,2,3,"Turkey",(5,6,7)} set of mixed datatype


# my_Set2 = set("Ali","Kerem","Buse")
my_StudentsSet = {"Berkay", "Merve", "Derin", "Nermin"}
print(my_StudentsSet), print("---------------")  # Randomly Ordering

for student in my_StudentsSet:
    print(student)

print("---------------")
print("Berkay" in my_StudentsSet), print(
    "berkay" in my_StudentsSet), print("---------------")

my_StudentsSet.add("Ahmet"), print(my_StudentsSet), print("---------------")
my_StudentsSet.update(["Selin", "Büşra"]), print(
    my_StudentsSet), print("---------------")  # Multiple insertion
my_StudentsSet.remove("Ahmet"), my_StudentsSet.discard("Büşra"), print(
    my_StudentsSet), print(len(my_StudentsSet)), print("---------------")
my_StudentsSet.pop(), print(my_StudentsSet), print(
    len(my_StudentsSet)), print("---------------")
my_StudentsSet.clear(), print(my_StudentsSet), print(
    len(my_StudentsSet))  # my_StudentsSet is cleared
del my_StudentsSet  # Delete set


# %%  Sets Union , Intersection , Difference , Symmetric Difference

my_SetA = {1, 2, 3, 4, 5}
my_SetB = {1, 3, 4, 6, 7, 8}
print("A = "+str(my_SetA)), print("B = "+str(my_SetB)), print("-----------")
# or print(my_SetA | my_SetB)  or print(my_SetB.union(my_SetA))
print("A union B = "+str(my_SetA.union(my_SetB)))
# or print(my_SetA & my_SetB)  or print(my_SetA.intersection(my_SetB))
print("A intersection B = "+str(my_SetA.intersection(my_SetB)))
# or print(my_SetA - my_SetB)
print("A difference B = "+str(my_SetA.difference(my_SetB)))
# or print(my_SetB - my_SetA)
print("B difference A = "+str(my_SetB.difference(my_SetA)))
# or print(my_SetA ^ my_SetB)
print("A symmetric difference B = "+str(my_SetA.symmetric_difference(my_SetB)))
# or print(my_SetB ^ my_SetA)
print("B symmetric difference A = "+str(my_SetB.symmetric_difference(my_SetA)))
