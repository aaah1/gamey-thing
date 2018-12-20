'''
Created on Oct 29, 2018

@author: 804023001
'''
import pygame
from pygame import *
pygame.init()
class Character(pygame.sprite.Sprite):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """
 
    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its size. """
 
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
        
run=True
plyrx=50
plyry=100
l=20
w=20
vel=5
screen = display.set_mode((800,600))
enemylist = pygame.sprite.Group()
allsprites=pygame.sprite.Group()
clock=time.Clock()
score=0

for x in range (10):
    block =Character([255, 0, 255], 20, 15)
    block.rect.x = (10*x) 
    block.rect.y = (20*x)
    enemylist.add(block)
    allsprites.add(block)
player=Character([50,50,50],10,10)
allsprites.add(player)
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

    player.rect.x=plyrx
    player.rect.y=plyry
    
    hitlist=sprite.spritecollide(player, enemylist, True) 
    for block in hitlist:
        score += 1
        print(score)
    
    screen.fill((255, 255, 255))
    allsprites.draw(screen)
    display.flip()
    clock.tick(60)