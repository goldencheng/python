# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 15:34:45 2021

@author: twson
"""

e=float(input('math?'))
s=float(input('english?'))
while s>100 or e>100 or s<0 or e<0:
    print("no way!")
    e=float(input('math?'))
    s=float(input('english?'))
if 100>=s>=90 and 100>=e>=90:
   print("money!!")
else:
    if s<=59 and e<=59:
        print("NO!!!")
    else:
        if s<=59 or e<=59:
            print("QQ")
        else:
            if s<100 and e<100:
                print("nothing")

        



    