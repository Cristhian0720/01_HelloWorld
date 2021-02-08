# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

lista=[]
file=open("devices.txt")
for item in file:
    item=item.strip()
    print(item)
file.close
print(lista)