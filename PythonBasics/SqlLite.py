#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 19:26:28 2021
@author: berkay
"""

import sqlite3

connection = sqlite3.connect("SampleDatabase.db")  # connect to database file

# %% select , from , where , or , and , desc ,order by

cursor = connection.execute("""select FirstName,LastName 
                            from customers 
                            where city = 'Prague' or city = 'Berlin' order by FirstName,LastName desc""")

for row in cursor:
    print("FirstName : "+row[0])
    print("LastName : "+row[1])
    print("***********")

# %% Group by , having

cursor2 = connection.execute("""
                             select city,count(*) from customers
                             group by city having count(*)>1
                             order by count(*) desc
                             """)

for row in cursor2:
    print("City Name :"+row[0])
    print("Count : "+str(row[1]))
    print("***********")

# %% Like

cursor3 = connection.execute("""
                             select FirstName,LastName from customers
                             where FirstName like '%a'
                             """)

for row in cursor3:
    print("FirstName : "+row[0])
    print("LastName : "+row[1])
    print("***********")
    
# %% Insert

def insertCustomer():
    connection = sqlite3.connect("SampleDatabase.db") 
    connection.execute("""
                       insert into customers (firstName,lastName,city,email)
                       values("Berkay","Çiftçi","Aydın","c.berkay@outlook.com")
                       """)
    connection.commit()
    connection.close()
                       
insertCustomer()

# %% Update    Aydın to Change İstanbul

def updateCustomer():
    connection = sqlite3.connect("SampleDatabase.db") 
    connection.execute("""
                       update customers set city = 'İstanbul' where city = 'Aydın'
                       """)
    connection.commit()
    connection.close()

updateCustomer()

# %% Delete 

def deleteCustomer():
    connection = sqlite3.connect("SampleDatabase.db") 
    connection.execute("""
                       Delete from customers 
                       where city = 'İstanbul' 
                       """)
    connection.commit()
    connection.close()

deleteCustomer()

# %% Join 

def joinCustomer():
    connection = sqlite3.connect("SampleDatabase.db") 
    cursor4 = connection.execute("""
                       select albums.Title,
                       artists.Name from artists 
                       inner join albums 
                       on artists.ArtistId = albums.ArtistId
                       """)
   
    for row in cursor4:
        print("Title : "+row [0]+" Name : "+row[1])
           
    connection.close()
    
joinCustomer()