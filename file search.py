# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 14:50:21 2021

@author: twson
"""
t=str(input("?"))
import os.path as d
if d.isfile(t):
    print('found')
else:
    print('no')