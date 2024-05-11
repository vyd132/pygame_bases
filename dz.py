import time

import pygame
from pygame import display
import random

def t_spawn():
    tank=pygame.image.load('tank_enemy_size1_green1.png')
    tank=pygame.transform.scale(tank,[tsize,tsize])
    return tank



screen=display.set_mode([500,500])

yspeed=-3
xspeed=3

c=random.randint(200,400)

a=pygame.Rect([100,100,c,c])

tsize=random.randint(10,50)

tank_rect1=pygame.Rect([100,100,tsize,tsize])
tank_rect2=pygame.Rect([100,100,tsize,tsize])
tank_rect3=pygame.Rect([100,100,tsize,tsize])
tank_rect4=pygame.Rect([100,100,tsize,tsize])
tank_rect5=pygame.Rect([100,100,tsize,tsize])
tank_rect6=pygame.Rect([100,100,tsize,tsize])
tank_rect7=pygame.Rect([100,100,tsize,tsize])
tank_rect8=pygame.Rect([100,100,tsize,tsize])
tank_rect9=pygame.Rect([100,100,tsize,tsize])

tank_angle1=pygame.Rect([100,100,tsize,tsize])


angle=0

t2=t_spawn()


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
    t1 = pygame.transform.rotate(t2, angle)
    tank_angle1.width=t1.get_width()
    tank_angle1.height=t1.get_height()


    tank_rect1.centerx=a.centerx
    tank_rect1.centery = a.centery
    tank_rect2.x=a.x
    tank_rect2.y = a.y
    tank_rect3.right=a.right
    tank_rect3.top = a.top
    tank_rect4.x=a.x
    tank_rect4.bottom=a.bottom
    tank_rect5.right=a.right
    tank_rect5.bottom=a.bottom
    tank_rect6.centerx = a.centerx
    tank_rect6.y = a.y
    tank_rect7.centerx = a.centerx
    tank_rect7.bottom = a.bottom
    tank_rect8.x = a.x
    tank_rect8.centery = a.centery
    tank_rect9.right = a.right
    tank_rect9.centery = a.centery
    tank_angle1.centerx=a.centerx
    tank_angle1.centery = a.centery


    time.sleep(1/60)
    screen.fill([0,0,0])
    pygame.draw.rect(screen,[255, 0,0], a)
    pygame.draw.circle(screen, [255, 255, 0],[ a.centerx,a.centery],c/2)
    pygame.draw.rect(screen, [255, 0, 0], tank_rect1)
    pygame.draw.rect(screen, [255, 0, 0], tank_rect2)
    pygame.draw.rect(screen, [255, 0, 0], tank_rect3)
    pygame.draw.rect(screen, [255, 0, 0], tank_rect4)
    pygame.draw.rect(screen, [255, 0, 0], tank_rect5)
    pygame.draw.rect(screen, [255, 0, 0], tank_rect6)
    pygame.draw.rect(screen, [255, 0, 0], tank_rect7)
    pygame.draw.rect(screen, [255, 0, 0], tank_rect8)
    pygame.draw.rect(screen, [255, 0, 0], tank_rect9)

    screen.blit(t1, tank_angle1)
    r=pygame.Rect(tank_rect1.x,tank_rect1.y,t1.get_width(),t1.get_height())
    pygame.draw.rect(screen,[0,0,0],r,2)
    screen.blit(t1, tank_rect2)
    screen.blit(t1, tank_rect3)
    screen.blit(t1, tank_rect4)
    screen.blit(t1, tank_rect5)
    screen.blit(t1, tank_rect6)
    screen.blit(t1, tank_rect7)
    screen.blit(t1, tank_rect8)
    screen.blit(t1, tank_rect9)

    pygame.display.flip()

    pass