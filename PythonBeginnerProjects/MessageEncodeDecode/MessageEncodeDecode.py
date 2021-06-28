#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 19:26:28 2021
@author: berkay
"""
# Importing Modules
from tkinter import *
import base64  as b64

# Initialize window and Title of the window
window = Tk()
window.title("Message Encode And Decode App ")
window.geometry("500x300")
window.resizable(0,0)

# Label
Label(window, text='ENCODE DECODE', font='Roboto 28 ').pack(side=TOP)
Label(window, text='Made By Berkay Ç.', font='Roboto 14 ').pack(side=BOTTOM)

# Define Variables
Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()

# Function to Encode

def Encode(key, message):
    enc = []    
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
        
    return b64.urlsafe_b64encode("".join(enc).encode()).decode()

# Function to Decode
def Decode(key, message):
    dec = []
    message = b64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))
    return "".join(dec)

# Function to Set Mode
def Mode():
    if(mode.get() == 'e'):
        Result.set(Encode(private_key.get(), Text.get()))
    elif(mode.get() == 'd'):
        Result.set(Decode(private_key.get(), Text.get()))
    else:
        Result.set("Invalid Mode")

# Function to Exit Window
def Exit():
    window.destroy()

# Function to reset
def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")

# Message Label And Entry
Label(window, text='Message : ', font='Roboto 10 ').place(x=20, y=60)
Entry(window, font='Roboto 12', textvariable=Text, bg="white").place(x=270, y=60)

# Key Label And Entry
Label(window, text='Key : ', font='Roboto 10 ').place(x=20, y=90)
Entry(window, font='Roboto 12', textvariable=private_key,bg="white").place(x=270, y=90)

# Mode Label And Entry
Label(window, text='Mode(Encode-e,Decode-d :)', font='Roboto 10 ').place(x=20, y=120)
Entry(window, font='Roboto 12', textvariable=mode,bg="white").place(x=270, y=120)

# Result Button And Entry
Button(window, font="Roboto 12", text='RESULT', padx=2,bg='Lime Green', command = Mode).place(x=20, y=150)
Entry(window, font='Roboto 12', textvariable=Result,bg="white").place(x=270, y=150)

# Reset Button And Entry
Button(window, font="Roboto 12", text="RESET", padx=2,bg='Blue', command=Reset).place(x=160, y=200)
Button(window, font="Roboto 12", text="EXİT", padx=2,bg='Red', command=Exit).place(x=240, y=200)


window.mainloop()
