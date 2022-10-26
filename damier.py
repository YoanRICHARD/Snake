import sys
import pygame

pygame.init()
screen = pygame.display.set_mode([600, 600])
clock = pygame.time.Clock()

x = -40
width = 20
height = 20
red = 255
green = 255
blue = 255
color = [red, green, blue]
for i in range (15):
    x += 40
    y = -40
    for j in range (15):
        y += 40
        rect = [x, y, width, height]
        pygame.draw.rect(screen, color, rect)
x = -20
for i in range (15):
    x += 40
    y = -20
    for j in range (15):
        y += 40
        rect = [x, y, width, height]
        pygame.draw.rect(screen, color, rect)

red = 30
green = 155
blue = 10
color = [red, green, blue]
y = 300
x = 200
width = 60
height = 20
rect = [x, y, width, height]
pygame.draw.rect(screen, color, rect)
pygame.display.update()


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
                print ("↑")
            if event.key == pygame.K_LEFT:
                print ("←")
            if event.key == pygame.K_DOWN:
                print ("↓")
            if event.key == pygame.K_RIGHT:
                print ("→")
                  

