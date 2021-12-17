# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 14:29:50 2021

@author: twson
"""
file=open('eee.txt','r')
file=file.read()

ex={}

print(ex)
import os.path as q
import time as o
print('我是PYTHON CAT 1.0,喵!',end='')
o.sleep(1)
p=int(input("是否要教學?1要2不要"))
if p==1:
    print('教我說話:','learn,x,enter,y')
    print('已教了:','teach')
    print('時間:','time')
    print('離開:','out')
    print('說話:','x')
    print('刪除:','erase,enter,x')
    print('計算機:','math,X,enter,運算符號,y\n(有加法+，減-，乘*，除/，次方**，取餘數%)')
    print('關於我(教學):','pyton cat 或 你是誰?')
    print('儲存:','save')
    w=input('以閱讀完成請按enter，喵')
while True:
     
     e=str(input("輸入"))
     o.sleep(1)
     if e=="time":
         print(o.asctime())
     elif e =='learn':
          f=str(input("喵?"))
          o.sleep(1)
          
          if f in file or f in ex:
               print("喵，我學過了!")
               
          else:
               t=str(input("喵?"))
               ex[f]=t
               print('喵!知道了!')
     elif e=='teach':
         for i,j in ex.items():
             print('你說:',i,'喵說:',j)
     elif e=='out':
         print("再見!喵!")
         break    
     elif e in ex:
         print(ex[e],'，喵!')
     elif e=="erase":
         hj=str(input("喵?"))
         if hj in ex:
             ex.pop(hj)
             print("好喔，喵!")
     elif e=="math":
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

     elif e=="python cat" or e=='你是誰?':
          print('我是Python cat\n我的設計者是Golden cheng\n我的生日是2021/11/13')
          print('教我說話:','learn,x,enter,y')
          print('已教了:','teach')
          print('時間:','time')
          print('離開:','out')
          print('說話:','x')
          print('刪除:','erase,enter,x')
          print('計算機:','math,X,enter,運算符號,y\n(有加法+，減-，乘*，除/，次方**，取餘數%)')
          print('關於我(教學):','pyton cat 或 你是誰?')
    
     elif e=="save":
          if not q.isfile('eee.txt'):
              popo=open('eee.txt','w')
          else:
              popo=open('eee.txt','a')
          for i,j in ex.items():
              popo.write(i)
              popo.write(':')
              popo.write(j)
          popo.close()
              
     else:
         print("不懂，喵?")
            
                    
      
                
            
      
        
    

    