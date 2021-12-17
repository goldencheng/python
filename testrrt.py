# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 15:19:42 2021

@author: twson
"""

def iii():
    t=str(input("?"))
    t=t+'.txt'
    import os.path as d
    if d.isfile(t):
        print('found')
    else:
        print('no')
        file=open(t,'a')
        file.write("test")
        
        file=open(t,'r')
        print(file.read())
        file.close()    