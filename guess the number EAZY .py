# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 14:59:05 2021

@author: twson
"""
e=float(input('1~10?'))
import random
ff=random.randint(1,10)
while e!=ff:
    print('no')
    e=float(input('?'))
else :
    print('yes is ')
print(ff)