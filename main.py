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
mario=pygame.image.load('mario.png')
princ=pygame.image.load('princess.png')
princ=pygame.transform.flip(princ,True,True)
mario=pygame.transform.scale(mario,[100,100])



sun=pygame.Surface([100,100],pygame.SRCALPHA)
pygame.draw.rect(sun,[112,205,255],[0,0,100,100])
pygame.draw.circle(sun,[255,241,16],[50,50],20)
pygame.draw.line(sun,[255,241,16],[0,50],[100,50],width=5)
pygame.draw.line(sun,[255,241,16],[50,50],[50,0],width=5)
pygame.draw.line(sun,[255,241,16],[50,50],[50,100],width=5)
pygame.draw.line(sun,[255,241,16],[50,50],[0,0],width=7)
pygame.draw.line(sun,[255,241,16],[50,50],[100,100],width=7)
pygame.draw.line(sun,[255,241,16],[50,50],[100,0],width=7)
pygame.draw.line(sun,[255,241,16],[50,50],[0,100],width=7)
pygame.image.save(sun,'sun.jpg')

sun=pygame.transform.rotate(sun,200)

pygame.draw.rect(screen,[0,255,0],[0,400,500,100])
pygame.draw.rect(screen,[112,205,255],[0,0,500,400])
screen.blit(mario,[40,310])
screen.blit(princ,[340,320])
screen.blit(sun,[400,0])

pygame.display.flip()

while True:
    pass

