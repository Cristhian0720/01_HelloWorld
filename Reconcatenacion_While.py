# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 14:25:48 2021

@author: Cristhian Tipan
"""

while True:
    x=input("Ingrese un numero para contar: ")
    if x == 'q' or x == 'quit':
        break

    x=int(x)
    y=1
    while True:
        print(y)
        y=y+1
        if y>x:
            break
