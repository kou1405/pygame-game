from pygame.locals import *
import pygame
from random import randint
o=15
i=7
lo=0
def k(x,y,p,i,o,lo):
    fenetre.fill((0,0,0))
    pygame.draw.rect(fenetre,(255,200,255),(x,y,i,o))
    pygame.draw.circle(fenetre, (255, 255, 255), (p, p), 7 )
    pygame.display.flip()
    pygame.display.update()
    if (int (x),int(y))==(p,p):
        p=randint(100,500)
        o+=1
        lo+=1
        print(lo)
    return p,o,i
        
x,y=250,250
p=randint(100,500)
pygame.init()
WHITE = (255, 255, 255)
fenetre = pygame.display.set_mode((600,580))
pygame.display.set_caption("دودة ")
c=True
pygame.mixer.music.load("k.aac")
def h(p,i,x,y,lo):
    if p-5<=int (x)<=p+5 and p-5<=int(y)<=p+5:
        p=randint(100,500)
        i+=10
        lo+=1
        print(lo)
    return p,i,lo
w,b,v,q=0,0,0,0
def mer(o,i,w):
    if w!=1:
        a=o
        o=i
        i=a
        w=1
    return o,i,w
pygame.mixer.music.play()
while c:
    for e in pygame.event.get():
        if e.type==pygame.KEYDOWN :
            """if e.key==pygame.K_LEFT:
                while 1:
                    x-=0.1
                    p,o,i=k(x,y,p,i,o)
                    print(pygame.event.get())
                    if len(pygame.event.get())>0 or not(0<=x<=500):
                        break
            if e.key==pygame.K_RIGHT:
                while 1:
                    x+=0.1
                    p,o,i,lo=k(x,y,p,i,o,lo)
                    print(pygame.event.get())
                    if len(pygame.event.get())>0 or not(0<=x<=500):
                        break
            if e.key==pygame.K_DOWN:
                while 1:
                    y+=0.1
                    p,o,i,lo=k(x,y,p,i,o,lo)
                    print(pygame.event.get())
                    if len(pygame.event.get())>0 or not(0<=y<=580):
                        break
                  
            if e.key==pygame.K_UP:
                while 1:
                    y-=0.1
                    p,o,i,lo=k(x,y,p,i,o,lo);print(pygame.event.get())
                    if len(pygame.event.get())>0 or not(0<=y<=500):
                        break"""
            if e.key==pygame.K_SPACE:
                c=False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if x>500:
             x=0
        elif x<0:
             x=500
        x-=0.1
        o,i,w=mer(o,i,w)
        p,i,lo=h(p,i,x,y,lo)
        
    if not(keys[pygame.K_LEFT]):
        w=0
    if keys[pygame.K_RIGHT]:
         if x>580:
             x=0
         elif x<0:
             x=500
         x+=0.1
         o,i,q=mer(o,i,q)
         p,i,lo=h(p,i,x,y,lo)
        
          
    if not(keys[pygame.K_RIGHT]):
        q=0
         
    if keys[pygame.K_UP]:
        if y>580:
             y=0
        elif y<0:
             y=580
        y-=0.1
        o,i,v=mer(o,i,v)
        p,o,lo=h(p,o,x,y,lo)
    if not(keys[pygame.K_UP]):
        v=0
        
    if keys[pygame.K_DOWN]:
        if y>580:
             y=0
        elif y<0:
             y=580
        y+=0.1
        o,i,b=mer(o,i,b)
        p,o,lo=h(p,o,x,y,lo)
    if not(keys[pygame.K_DOWN]):
        b=0
    fenetre.fill((0,0,0))
    pygame.draw.rect(fenetre,(255,200,255),(x,y,i,o))
    pygame.draw.circle(fenetre, WHITE, (p, p), 5)
    pygame.display.flip()
    pygame.display.update()
pygame.quit()
print("fin du jeu")
 
