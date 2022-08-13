# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 20:07:09 2022

@author: Juliano
"""

import os

print('Informes os 3 lados do triângulo:')

a = float(input('Lado 1: '))

b = float(input('Lado 2: '))

c = float(input('Lado 3: '))

if (a > b + c) or (b > a + c) or (c > a + b):
    
     print('Estas medidas não formam um triângulo!')
else:
 if (a == b) and (b == c):
     print('Este é um triângulo equilátero')
 elif (a == b) or (b == c) or (a == c):
     print('Este é um triângulo isósceles')
 else:
     print('Este é um triângulo escaleno')
 
 os.system('pause')