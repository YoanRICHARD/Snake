import sys
import pygame
import random

pygame.init()
screen = pygame.display.set_mode([600, 600])
clock = pygame.time.Clock()

snake = [[10, 15], [11, 15], [12, 15]]
red = 30
green = 155
blue = 10
color = [red, green, blue]
vecteur = [1, 0]
width = 20
height = 20
white = [255, 255, 255]
black = [0, 0, 0]
while True:
    x = -40
    for i in range(15):
        x += 40
        y = -40
        for j in range(15):
            y += 40
            rect = [x, y, width, height]
            pygame.draw.rect(screen, white, rect)
    x = -20
    for i in range(15):
        x += 40
        y = -20
        for j in range(15):
            y += 40
            rect = [x, y, width, height]
            pygame.draw.rect(screen, white, rect)
    x = -20
    for i in range(15):
        x += 40
        y = -40
        for j in range(15):
            y += 40
            rect = [x, y, width, height]
            pygame.draw.rect(screen, black, rect)
    x = -40
    for i in range(15):
        x += 40
        y = -20
        for j in range(15):
            y += 40
            rect = [x, y, width, height]
            pygame.draw.rect(screen, [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)], rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
    for x, y in snake:
        rect = [x * 20, y * 20, 20, 20]
        pygame.draw.rect(screen, color, rect)
    for t in snake:
        t[0], t[1] = t[0] + vecteur[0], t[1] + vecteur[1]
    pygame.display.update()
    clock.tick(1)
