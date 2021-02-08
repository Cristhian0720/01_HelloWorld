# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 13:33:41 2021

@author: Cristhian Tipan
"""


file=open("devices.txt","a")

while True:
    newItem=input("new line: ")
    if newItem =="exit":
        print("ALL DONE!")
        break
    else:
        file.write(newItem+"\n")    
file.close


   