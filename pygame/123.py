import pygame
pygame.init()
fenetre = pygame.display.set_mode((1000,100),pygame.FULLSCREEN)
pygame.display.set_caption("koussay jeux")
image=pygame.image.load("koussay.jpg").convert_alpha()
pygame.display.set_icon(image)
fenetre.blit(image,(0,1000))
c=True
while c:
    fenetre.blit(image,(0,0))
    #pour plusieur evenement car il return une liste
    for e in pygame.event.get():
        if e.type==pygame.KEYUP:
            c=False
     #pour un seul evenement car il return la premiere evenement
   #if pygame.event.wait().type==pygame.KEYDOWN:
        #c=False
    
    pygame.display.flip()
   
pygame.quit()
