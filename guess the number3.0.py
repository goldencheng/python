# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 16:18:29 2021

@author: twson

"""
ppo=int(input('range1?'))
q=int(input('range2?'))
pp=int(input('chance?'))


import random
SECRET1=random.randint(ppo,q)
(type(float(SECRET1)))
EEEE = q
print('guess a numbur',end='')
print(ppo,end='')
print('~',end='')
print(q,end='')
print('.')
print('you have ',end='')
print(pp,end='')
print(" times to guess!!")


ans = float(input('enter'))
for i in range(pp-1):
        if SECRET1!=ans :
            
            if ans > EEEE:
                print('out of the range and ')
            if ans > SECRET1:
                print('too big!')
                ans = int(input('guess'))
            if ans < SECRET1:
                print('too small!')
                ans = int(input('guess'))
if SECRET1==ans:
    print('you win!')
    print('anser is ',end='')
    print(SECRET1)
else:
    print('you lose!')
    print('anser is',end='')
    print(SECRET1)
    
    


      
        
         

    




         
    
        
    
        
       

