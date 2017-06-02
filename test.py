import pygame
import sys
import time

from pygame.locals import *

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

width = 400
height = 300
DISPLAYSURF = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption('Animation')
background = pygame.image.load('bg.png')

UP = 'up'
LEFT = 'left'
RIGHT = 'right'
DOWN = 'down'

sprite = pygame.image.load('down.png')
spritex = 200
spritey = 130
direction = None


def move(direction, sprite, spritex, spritey):
    if direction:

        if direction == K_UP:
            spritey -= 1
            sprite = pygame.image.load('up.png')
        elif direction == K_DOWN:
            spritey += 1
            sprite = pygame.image.load('down.png')
        elif direction == K_LEFT:
            spritex -= 1
            sprite = pygame.image.load('left.png')
        elif direction == K_RIGHT:
            spritex += 1
            sprite = pygame.image.load('right.png')
    return sprite, spritex, spritey


# pygame.mixer.music.load('bgm.mp3')
# pygame.mixer.music.play(-1, 0.0)
while True:
    DISPLAYSURF.blit(background, (0, 0))

    DISPLAYSURF.blit(sprite, (spritex, spritey))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            direction = event.key
        if event.type == KEYUP:
            if event.key == direction:
                direction = None
    sprite, spritex, spritey = move(direction, sprite, spritex, spritey)

    pygame.display.update()
    fpsClock.tick(FPS)
