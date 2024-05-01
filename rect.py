import time

import pygame
from pygame import display
import random

screen=display.set_mode([500,500])

yspeed=-3
xspeed=3

a=pygame.Rect([200,100,130,40])
a.x=300
a.right=500
a.centerx=250
a.w=200


while True:
    time.sleep(1/60)
    screen.fill([0,0,0])
    pygame.draw.rect(screen,[255, 0,255], a)
    a.top+=yspeed
    if a.top<=0:
        a.top = 0
        yspeed=5
    if a.bottom >= 500:
        a.bottom= 500
        yspeed = -5
    a.right+=xspeed
    if a.left>=500:
        a.right=0

    pygame.display.flip()
    pass