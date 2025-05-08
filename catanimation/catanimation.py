import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 60 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
catImg = pygame.image.load('cat.png')
catx1 = 10
caty1 = 10
catx2 = 10
caty2 = 10
direction1 = 'right'
direction2 = 'down'

while True: # the main game loop
    DISPLAYSURF.fill(WHITE)

    if direction1 == 'right':
        catx1 += 5
        if catx1 == 280:
            direction1 = 'down'
    elif direction1 == 'down':
        caty1 += 5
        if caty1 == 220:
            direction1 = 'left'
    elif direction1 == 'left':
        catx1 -= 5
        if catx1 == 10:
            direction1 = 'up'
    elif direction1 == 'up':
        caty1 -= 5
        if caty1 == 10:
            direction1 = 'right'

    if direction2 == 'down':
        caty2 += 5
        if caty2 == 220:
            direction2 = 'right'
    elif direction2 == 'right':
        catx2 += 5
        if catx2 == 280:
            direction2 = 'up'
    elif direction2 == 'up':
        caty2 -= 5
        if caty2 == 10:
            direction2 = 'left'
    elif direction2 == 'left':
        catx2 -= 5
        if catx2 == 10:
            direction2 = 'down'

    DISPLAYSURF.blit(catImg, (catx1, caty1))
    DISPLAYSURF.blit(catImg, (catx2, caty2))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)