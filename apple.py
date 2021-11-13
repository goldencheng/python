# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 14:42:33 2021

@author: twson

"""
ssj=0
import time as o
print('歡迎使用money計價程式')
o.sleep(0.5)
print('正在加載......')
o.sleep(3)
s=int(input('1.庫存 2.進貨 3.出貨 4.營業額統計 5.離開系統 6.設定'))
while s!=6:
    print('請先設定!')
    s=int(input('1.庫存 2.進貨 3.出貨 4.營業額統計 5.離開系統 6.設定'))

if s==6:
   g=int(input('庫存?'))
   o.sleep(0.5)
   d=int(input('單價?'))
   o.sleep(0.5)
   print('設定ok')
while s==6:
    while s==6 or s==7:
        s=int(input('1.庫存 2.進貨 3.出貨 4.營業額統計 5.離開系統 6.設定'))
        if g==0 :
            print("!警告!:你的庫存已歸零")
            o.sleep(0.5)
        if g<0 :
            print("!警告!:你已負債(庫存)")
            o.sleep(0.5)
        if 0-g>10:
            print("!警告!:你已嚴重負債(庫存)")
            o.sleep(0.5)
        if s==6:
            g=int(input('庫存?'))
            o.sleep(0.5)
            d=int(input('單價?'))
            o.sleep(0.5)
            print('設定ok')
            s=7
        if s==2:
           f=int(input('+?'))
           g=g+f
           print('庫存:',end='')
           o.sleep(0.5)
           print(g)
          
           s=7
        if s==3:
           t=int(input('-?'))
           ssj=ssj+t*d
           g=g-t
           print('庫存:',end='')
           o.sleep(0.5)
           print(g)
           print('賺:',end='')
           o.sleep(0.5)
          
           print(t*d)
           s=7
        if s==4:
            print('今天賺了:',end='')
            o.sleep(0.5)
            print(ssj)
            s=7
        if s==1:
            print('庫存:',end='')
            o.sleep(0.5)
            print(g)
            s=7
        if s==5:
            print('謝謝使用')
            break
        if 