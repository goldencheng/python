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
    print('教我說話:','l,x,enter,y')
    print('已教了:','s')
    print('時間:','t')
    print('離開:','o')
    print('說話:','x')
    w=input('以閱讀完成請按enter，喵')
while True:
     e=str(input("輸入"))
     o.sleep(1)
     if e=="t":
         print(o.asctime())
     if e =='l':
          f=str(input("喵?"))
          o.sleep(1)
          if f not in ex:
               t=str(input("喵?"))
               ex[f]=t
               print('喵!知道了!')
          else:
               
               print("喵，我學過了!")
     if e=='s':
         
         for i,j in ex.items():
             
             print('你說:',i,'喵說:',j)
     if e=='o':
         
         print("再見!喵!")
         break    
     if e in ex:
         
         print(ex[e])
     
         
            
                    
      
                
            
      
        
    

    