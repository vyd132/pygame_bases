import pygame
from pygame import display

screen=display.set_mode([500,500])

b=pygame.image.load('player.png')
pygame.draw.circle(b,[255,0,0],[100,50],10)

a=pygame.Surface([100,100])
a.fill([255,255,255])
pygame.draw.line(a,[255,255,0],[10,50],[50,50])
pygame.draw.rect(a,[255,0,255],[20,30,40,50],2)
pygame.draw.circle(a,[0,255,255],[50,50],20)

pygame.image.save(a,'a.jpg')
b.blit(a,[50,0])
pygame.image.save(b,'b.png')

print(a)

pygame.draw.rect(screen,[255,0,255],[20,30,40,50])
pygame.display.flip()

while True:
    pass

