# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 14:34:14 2020

@author: Cristhian Tipan
"""
Nombre= input("Ingrese su nombre: ")
Apellido= input("Ingrese su apellido: ")
Edad= int(input("Ingrese su edad: "))
Lugar=input("Ingrese su lugar: ")
Space=" "
print(Space)
print("Hola, su nombre es",Space,Nombre,Space,"su apellido es",Space,Apellido,"usted tiene",Edad,"años",Space,"usted es de",Space,Lugar)
print(Space)
if Edad>=1 and Edad<=20:
    print("Usted es Joven")
elif Edad>=21 and Edad<=40:
    print("Usted es Señor") 
else: 
    print("Usted es Mayor")