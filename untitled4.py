# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 15:21:28 2021

@author: twson
"""

scores = []
ww=int(input("人?"))
for i in range(ww):
    y=int(input("?"))
    scores.append(y)
#最大值
print('第一:')
print(max(scores))
#最小值
print('')
print(min(scores))

#排序
print('第一最後:')
print(sorted(scores))
#列表長度
print('第一:')
print(len(scores))
#總和
print('第一:')
print(sum(scores))

