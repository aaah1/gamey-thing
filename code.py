'''
Created on Oct 29, 2018

@author: 804023001
'''
import pygame
from pygame import *
pygame.init()
run=True
plyrx=50
plyry=100
l=20
w=20
vel=1
screen = display.set_mode((800,600))

#-#-#-#-- main loop --#-#-#-#
while run:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            run=False
    keys=key.get_pressed()
    if keys[K_LEFT]:
        plyrx-=vel
    if keys[K_RIGHT]:
        plyrx+=vel
    if keys[K_UP]:
        plyry-=vel
    if keys[K_DOWN]:
        plyry+=vel
    
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (255, 0, 255), pygame.Rect(plyrx, plyry, l, w) )
    display.flip()