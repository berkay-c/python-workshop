#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 11:50:19 2021
@author: berkay
"""
# Lists
# my_list = []   Empty List
# my_list = [1,2,3,5]   List of Integers
# my_list = ["Hello",2,3.4] List with mix datatypes
# my_secondList = [1 , 2 , ["Hello",2,3.4], ['t']] Nested List
students = []
# add students
students.append(input("Enter the name of the 1st student = "))
students.append(input("Enter the name of the 2st student = "))
students.append(input("Enter the name of the 3st student = "))
print(students)
# remove student
students.remove(input("Enter the name of the student you want to be removed from the list = "))
print(students)
students.insert(3, "Melih")
print(students)
# %% List Constructor
country = list(("Turkey", "China", "England", "Turkey"))
print(country)
# %% Other List Functions
print("Turkey count = "+str(country.count("Turkey")))
print("China index = "+str(country.index("China")))
print("Turkey index = "+str(country.index("Turkey")))
# print(country.clear())
print(country)
country.pop(3), print(country), country.insert(3, "Russia"), print(country)
copycountry = country.copy()
country.reverse(), print(
    "-----------"), print(country), print(copycountry), print("-----------")
# %% to combine country and copy country
country.extend(copycountry), print(country)
country.sort(), print(country)
# %% If we want to sort in reverse order
country.reverse(), print(country)
