import pygame
pygame.init()
fenetre = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("koussay jeux")
c=True
while c:
    for e in pygame.event.get():
        if e.type==pygame.MOUSEBUTTONUP:
            x,y=e.pos
            pygame.draw.rect(fenetre,(20,100,100),(x,y,20,20))
        if e.type==pygame.KEYUP:
            if e.key==pygame.K_f:
                c=False
    pygame.display.flip()
   
pygame.quit()


