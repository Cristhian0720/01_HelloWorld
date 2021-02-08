# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 14:19:50 2021

@author: Cristhian Tipan
"""

acl=int(input ('Ingrese la  # de ACL: '))
if acl >=1 and acl<=99:
    print('La ACL es estandar')
elif acl>=100 and acl<=199:
    print('La ACL es extendida')
else:
    print('El # ingresado no es de una ACL')