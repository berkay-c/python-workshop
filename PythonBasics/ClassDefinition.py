#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 19:26:28 2021
@author: berkay
"""

# CLASSES And SELF
# Allows us to keep common features and functions together

# %% Basics
class Mathematic:
    def add(self, num1, num2):  # The self parameter is a reference to the current instance of the class

        return num1+num2   # and is used to access variables that belongs to the class.

    def multiply(self, num1, num2):
        return num1*num2

    def minus(self, num1, num2):
        return num1-num2

    def division(self, num1, num2):
        return num1/num2


mat = Mathematic() 
mat2 = Mathematic()      # This is a INSTANTIATE

print(mat2.add(5, 6)),print(mat2.division(5, 6)),print(mat.minus(6, 5)),print(mat.multiply(8, 9))

# %% Inıt Function And Self Details

class Mathematic2:
    def __init__(self,num1,num2):
        self.numberone=num1
        self.numbertwo=num2
        print("Constructor is Work")
        
    def multiply(self):
        return self.numberone*self.numbertwo

    def minus(self):
        return self.numberone-self.numbertwo

    def division(self):
        return self.numberone/self.numbertwo

mat3 = Mathematic2(8, 4)
print("Division : "+str(mat3.division())+" Multiply : "+str(mat3.multiply()))

# %% Property

class Person:
    def __init__(self,firstName,lastName,Age):
        self.firstname=firstName
        self.lastName=lastName
        self.age = Age
        
        
persons = Person("Berkay", "Çiftçi", 20)
print("Name = "+str(persons.firstname)+" \nSurname = "+str(persons.lastName)+" \nAge = "+str(persons.age))

# %% Inheritance

class Worker(Person):
    def __init__(self,salary):
        self.salary = salary
        
    
class Customer(Person):
    def __init__(self,creditCardNumber):
        self.creditCardNumber = creditCardNumber    
    
worker1 = Worker(3450)
customer1=Customer(4543607195287418)

worker1.firstname="Kerem"  
customer1.age=28
