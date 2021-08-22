# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 10:26:22 2021

@author: twson
"""
e=float(input('point?'))

while e>100 or e<0:
   print("no way")
   e = int(input('point?'))
if 101>e>=90:
    print("a")
if 80<=e<90:
    print("b")
if 70<=e<80:
    print("c")
if 60<=e<70:
    print("d")
if e<=60:
    print("e")



    
