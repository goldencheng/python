# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 14:08:46 2021

@author: twson
"""

ex = {"w":[3,'www','hjhjh'],
      "q":1,
      "o":2,}
print(ex)
print(ex["w"])
print(ex["w"][1])
f={}
print(f)
f["w"]=20
print(f)

i = input('sss')
j=input('wi')
f[i]=j
print(f)
f2={'r':22,
    'w':67876,}
f.update(f2)
print(f)
for i in f.keys():
    print(i)
for i in f.values():
    print(i)
for i,j in f.items
():
    print("fff",i,"kll",j)
 
        