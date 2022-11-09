import sys
import pygame
import random

pygame.init()
screen = pygame.display.set_mode([600, 600])
clock = pygame.time.Clock()

##________paramètre initiaux_______________________________

vivant = 1
vitesse = 7/4

rs = random.randint(169-32, 169+32)
bs = random.randint(120-32,120+32)
couleur_serpent = [rs, 0, bs]
seconde_couleur = [rs-30, 0, bs-30]

serpent = [(10, 15), (11, 15), (12, 15)]
direction = [1,0]

fruit = (14, 15)

##__________________________________________________________

def is_bright(coordonnées):
    if (coordonnées[0]+coordonnées[1])%2==0:
        return [97, 198, 74] # couleur claire
    return [0, 163, 0] # couleur foncée

##____________Tracés________________________________________

for x in range (30):
    for y in range(30):
        pygame.draw.rect(screen, is_bright([x,y]), [20*x, 20*y, 20, 20])
pygame.display.update()

for z in serpent:
    pygame.draw.rect(screen, seconde_couleur, [20*z[0], 20*z[1], 20, 20])
    pygame.draw.rect(screen, couleur_serpent, [20*z[0]+1, 20*z[1]+1, 18, 18])


##__________________________________________________________

def Mouvement(snake, orientation):
    x,y = snake[-1]
    x = (x+orientation[0])%30
    y = (y+orientation[1])%30
    pygame.draw.rect(screen, seconde_couleur, [20*x, 20*y, 20, 20])
    pygame.draw.rect(screen, couleur_serpent, [20*x+1, 20*y+1, 18, 18])
    snake.append((x,y))
    if fruit != (x,y):
        queue = snake[0]
        pygame.draw.rect(screen, is_bright(queue), [20*queue[0], 20*queue[1], 20, 20])
        snake.pop(0)

##__________________________________________________________

##__________________________________________________________

while vivant:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                vitesse *= 7/8
            if event.key == pygame.K_f:
                vitesse *= 9/8
            if event.key == pygame.K_UP:
                if direction != [0, 1]:
                    direction = [0, -1]
                    break
            elif event.key == pygame.K_LEFT:
                if direction != [1, 0]:
                    direction = [-1, 0]
                    break
            elif event.key == pygame.K_DOWN:
                if direction != [0, -1]:
                    direction = [0, 1]
                    break
            elif event.key == pygame.K_RIGHT:
                if direction != [-1, 0]:
                    direction = [1, 0]
                    break
    Mouvement(serpent, direction)
    while fruit in serpent:
        fruit = (random.randint(0, 29), random.randint(0, 29))
    pygame.draw.rect(screen, [255, 20, 20], [20*fruit[0], 20*fruit[1], 20, 20])

    pygame.display.update()
    clock.tick(vitesse)

##__________________________________________________________
    
pygame.draw.rect(screen, [0, 0, 0], [0, 0, 600, 600])

while True:
    while vivant:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(25)