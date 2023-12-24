from pygame.locals import *
import pygame
pygame.init()
fenetre = pygame.display.set_mode((500,500),pygame.FULLSCREEN)
pygame.display.set_caption("koussay jeux")
image=pygame.image.load("k.png").convert_alpha()
pos=(0,0)
c=True
while c:
    for e in pygame.event.get():
        if e.type==pygame.MOUSEMOTION:
            pos=e.pos
        if e.type==pygame.KEYDOWN and e.key==pygame.K_SPACE:
            c=False
    pygame.draw.rect(fenetre,(255,255,255),(0,0,1000,1000))
    image.set_colorkey((255,255,0))
    fenetre.blit(image,pos)
    pygame.display.flip()
   
pygame.quit()

