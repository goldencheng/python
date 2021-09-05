# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 15:39:34 2021

@author: twson
"""
import random
SECRET1=random.randint(1,20)
EEEE = 20
print('guess a numbur 0-20.')
ans = int(input('guess'))
while SECRET1 != ans:
        if ans > EEEE:
            print('out of 20 and ')
        if ans > SECRET1:
            print('too big!')
        if ans < SECRET1:
            print('too small!')
        ans = int(input('guess'))
print('you got it! Is',end='')
print( SECRET1)