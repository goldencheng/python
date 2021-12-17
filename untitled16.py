# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 14:11:54 2021

@author: twson
"""
g="Abcdefghijklmnopqrstuvwxyz"
print(g[9])
print(g[-2])
print(g[4:6])
print(g[8:])
print(g[4:])
print(g[:7])
print(g[::3])
print(g[2:90:3])
print(g.capitalize())
print(g.title())
print(g.upper())
print(g.swapcase())
w=' g h j  h jj  nb bh njh bhn hgfiiiiiiif gf ftghjk'
print(w.split('i'))
print(w.split('h'))
print(w.split())
p='  gy  nj  kl  '
y='32  gy  nj  kl gh  gf00'
print(p.strip())
print(p.lstrip())
print(p.rstrip())
print(y.strip("3"))
print(w.count(" "))
print(w.count(" ",1,7))
print(w.replace("n","h"))
print(w.replace("n","h",1))