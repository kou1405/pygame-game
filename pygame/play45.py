import pygame
from pygame.locals import *

# Initialisation de Pygame
pygame.init()

# Définition des dimensions de la fenêtre
WIDTH = 800
HEIGHT = 600

# Couleurs
BLACK = (0, 0, 0)
WHITE = (25, 255, 255)

# Création de la fenêtre
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Déplacement d'objet")

# Position initiale de l'objet
x = WIDTH // 2
y = HEIGHT // 2

# Vitesse de déplacement de l'objet
vel = 5

# Boucle principale du jeu
running = True
while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Gestion des touches du clavier
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel

    # Effacer l'écran
    window.fill(BLACK)

    # Dessiner l'objet
    pygame.draw.rect(window, WHITE, (x, y, 50, 50))

    # Mettre à jour l'écran
    pygame.display.update()

# Fermer Pygame
pygame.quit()
print("fin du jeu")
