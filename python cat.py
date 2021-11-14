# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 14:29:50 2021

@author: twson
"""

ex={}
import time as o
print('我是PYTHON CAT 1.0,喵!',end='')
o.sleep(1)
g=int(input('是否閱讀教學?喵!1是2不用'))
if g==1:
    print('教我說話:','learn,x,enter,y')
    print('已教了:','teach')
    print('時間:','time')
    print('離開:','out')
    print('說話:','x')
    print('刪除:','erase,enter,x')
    print('計算機:','math,X,enter,運算符號,y\n(有加法+，減-，乘*，除/，次方**，取餘數%)')
    w=input('以閱讀完成請按enter，喵')
while True:
     e=str(input("輸入"))
     o.sleep(1)
     if e=="time":
         print(o.asctime())
     if e =='learn':
          f=str(input("喵?"))
          o.sleep(1)
          if f not in ex:
               t=str(input("喵?"))
               ex[f]=t
               print('喵!知道了!')
          else:
               print("喵，我學過了!")
     if e=='teach':
         for i,j in ex.items():
             print('你說:',i,'喵說:',j)
     if e=='out':
         print("再見!喵!")
         break    
     if e in ex:
         print(ex[e])
     if e=="erase":
         hj=str(input("喵?"))
         if hj in ex:
             ex.pop(hj)
             print("好喔，喵!")
     if e=="math":
         rr=float(input("喵?"))
         rt=str(input("喵?"))
         ww=float(input('喵?'))
         if rt=='+':
             print(rr+ww)
         if rt=='-':
             print(rr-ww)
         if rt=='**':
             print(rr**ww)
         if rt=='/':
             print(rr/ww)
         if rt=='*':
             print(rr*ww)
         if rt=='%':
             print(rr%ww)
    
         
            
                    
      
                
            
      
        
    

    