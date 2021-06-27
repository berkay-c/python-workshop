#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 19:26:28 2021
@author: berkay
"""
# %% Try Except and finally

try:
    number = int(input("Please Enter Number :"))
except ValueError:
    print("Entered Value Error")
except ZeroDivisionError:
    print("The Denominator Cannot Be Zero")
except:
    print("Something Wrong Happened")
finally:
    print("Finished")
   
# %% Recap Demo 5

import sys
list = ["Berkay",0,3,"6"]

for x in list:
    try: 
        print("Number "+ str(x))
        result = 1/int(x)
        print("Result : "+ str(result))
    except ValueError:
        print("This is not count")
    except:
        print(" Failed to calculate because : "+ str(sys.exc_info()[0]))
    