import random
import sys
import pygame

pygame.init()
screen = pygame.display.set_mode([1000, 700])
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_UP:
                print("↑")
            if event.key == pygame.K_LEFT:
                print("←")
            if event.key == pygame.K_DOWN:
                print("↓")
            if event.key == pygame.K_RIGHT:
                print("→")
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color = [red, green, blue]
    screen.fill(color)
    pygame.display.update()
    clock.tick(3)
