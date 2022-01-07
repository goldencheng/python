# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 19:05:18 2021

@author: twson
"""
import pygame
x=1
w,h=800,600
BLACK =(0, 0, 0)
WHITE =(255, 255, 255)
GREEN= (0,255,0)
RED = ( 255, 0, 0)
pygame.init()
PINK = pygame.color.Color ( "#FF87EE" )
y=pygame.color.Color('#e9ff01')
size=(700,500)





screen = pygame.display.set_mode(size)
pygame.display.set_caption("畫出一個圓心")
done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen. fill (WHITE)
    pygame.draw.circle(screen,y, [100,100],50)
    pygame.draw.circle(screen,BLACK,(80,90),10)
    pygame.draw.circle(screen,BLACK,(120,90),10)
    pygame.draw.lines(screen,BLACK,False,[(80,120),(120,120)], 3)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
