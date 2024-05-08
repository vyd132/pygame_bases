import time

import pygame
from pygame import display
import random

screen=display.set_mode([500,500])

yspeed=-3
xspeed=3

c=random.randint(200,400)

a=pygame.Rect([100,100,c,c])

tsize=random.randint(10,50)

tank_rect=pygame.Rect([100,100,tsize,tsize])

tank=pygame.image.load('tank_enemy_size1_green1.png')
tank=pygame.transform.scale(tank,[tsize,tsize])

angle=0

while True:
    angle+=1
    a.top += yspeed
    if a.top <= 0:
        a.top = 0
        yspeed = 5
    if a.bottom >= 500:
        a.bottom = 500
        yspeed = -5
    a.right += xspeed
    if a.left >= 500:
        a.right = 0
    tank_rect.centerx = a.centerx
    tank_rect.centery = a.centery

    time.sleep(1/60)
    screen.fill([0,0,0])
    pygame.draw.rect(screen,[255, 0,0], a)
    pygame.draw.circle(screen, [255, 255, 0],[ a.centerx,a.centery],c/2)
    pygame.draw.rect(screen, [255, 0, 0], tank_rect)
    # tank=pygame.transform.rotate(tank,angle)
    screen.blit(tank, tank_rect)
    pygame.display.flip()

    pass