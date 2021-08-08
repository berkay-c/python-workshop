#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 15:54:42 2021

@author: berkay
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
from flask import Flask

response = requests.get("https://www.ilimiz.net/il-plaka-kodlari.html")
# print(response.status_code) 200 döndü başarılı
soup = BeautifulSoup(response.content, "lxml")

data = soup.find_all("span", {"class": "sehir op"})
dataframe = pd.DataFrame(data, columns=["Şehir_Adı", "Boş", "Plaka_Kodu"])
geciciframe = dataframe.Plaka_Kodu.str.split(" ", expand=True)

geciciframe.columns = ["Plaka_Kodu", "Delete1", "Delete2"]
# İşimize yaramayacak olan sütünları bırakıyoruz
dataframe = dataframe.drop(columns=['Boş', 'Plaka_Kodu'])
geciciframe = geciciframe.drop(columns=["Delete1", "Delete2"])
# dataframe ile geciciframe birleştirip asıl temizlenmiş verilerimizi elde ediyoruz.
dataframe = pd.concat([dataframe, geciciframe], axis=1)
# Dataframe to csv  , does not pass index values
dataframe.to_csv("out.csv", index=False)
# print(dataframe.head())

# if it cannot find the database named 'my_database', it creates it
conn = sqlite3.connect('my_database.db')
c = conn.cursor()
# read out.csv
out = pd.read_csv("out.csv")
# "<strong> ve </strong> etiketlerini silmemiz gerekiyor.
out.Şehir_Adı = out.Şehir_Adı.str.replace('<strong>', '').str.replace("</strong>", "")
# print(out)

# if it cannot find the table named 'CityPlateCode', it creates it
out.to_sql("CityPlateCode", conn, if_exists='replace', index=False)
# print(pd.read_sql('''SELECT * FROM CityPlateCode''', conn))

# Flask ile web app oluşturma
app = Flask(__name__)


@app.route("/welcomepage")  # http://localhost:5000/welcomepage
def hello():
    return "Enter the license plate code or the name of the city in the URL field. <br/> Example:http://localhost:5000/welcomepage/46 OR http://localhost:5000/welcomepage/aydin"

@app.route("/welcomepage/<int:platecode>")
def PlateCode(platecode):
    while platecode<82 and platecode>0:
        vt = sqlite3.connect('my_database.db')
        cur = vt.cursor()
        cur.execute('''SELECT Şehir_Adı FROM CityPlateCode where Plaka_Kodu=?''', (platecode,))
        results = cur.fetchall()
        return f"{results}"
    return f"{platecode} Plate Codes Are Not Available! <br/> Please Enter A Valid License Plate Code"
       

@app.route("/welcomepage/<string:city>")
def CityName(city):
    city=city.upper()
    con = sqlite3.connect('my_database.db')
    cr = con.cursor()
    cr.execute("SELECT Plaka_Kodu FROM CityPlateCode WHERE Şehir_Adı like '%:cityname%' ", {"cityname":city,})
    dataresults = cr.fetchall()
    print(dataresults)
    return f"{dataresults}"
    

if __name__ == "__main__":
    app.run(host='localhost')  # http://localhost:5000
















