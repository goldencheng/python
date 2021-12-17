# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 22:29:49 2021

@author: twson
"""

import os.path as d
def math():
    o=float(input("喵?"))
    oo=str(input("喵?"))
   
    ooo=float(input("喵?"))    
    if oo=='+':
             y=o+ooo
    if oo=='-':
             y=o-ooo
    if oo=='**':
             y=o**ooo
    if oo=='/':
             y=o/ooo
    if oo=='*':
             y=o*ooo
    if oo=='%':
             y=o%ooo
    
    print(y)
def file_search():
    t=str(input("?"))
    t=t+'.py'
    if d.isfile(t):
        print(d.dirname(d.realpath(t)))
        print('found')
       
    else:
        print('no')
    