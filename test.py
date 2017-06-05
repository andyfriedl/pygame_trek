import pygame
import sys
import time

from pygame.locals import *

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

width = 1008
height = 710
DISPLAYSURF = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption('scifi Game Test')
background = pygame.image.load('space_port.gif')

UP = 'up'
LEFT = 'left'
RIGHT = 'right'
DOWN = 'down'

sprite = pygame.image.load('down.png')
sprite_x = width / 2
sprite_y = height / 2
direction = None


def move(direction_move, sprite_move, sprite_move_x, sprite_move_y):
    if direction:

        if direction_move == K_UP:
            sprite_move_y -= 2
            sprite_move = pygame.image.load('bot.png')
            # sprite_move = pygame.image.load('up.png')
        elif direction_move == K_DOWN:
            sprite_move_y += 2
            sprite_move = pygame.image.load('bot.png')
            # sprite_move = pygame.image.load('down.png')
        elif direction_move == K_LEFT:
            sprite_move_x -= 2
            sprite_move = pygame.image.load('bot.png')
            # sprite_move = pygame.image.load('left.png')
        elif direction_move == K_RIGHT:
            sprite_move_x += 2
            sprite_move = pygame.image.load('bot.png')
            # sprite_move = pygame.image.load('right.png')
    return sprite_move, sprite_move_x, sprite_move_y


# pygame.mixer.music.load('8-punk-8-bit-music.mp3')
# pygame.mixer.music.play(-1, 0.0)

while True:
    DISPLAYSURF.blit(background, (0, 0))

    DISPLAYSURF.blit(sprite, (sprite_x, sprite_y))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            direction = event.key
        if event.type == KEYUP:
            if event.key == direction:
                direction = None
    sprite, sprite_x, sprite_y = move(direction, sprite, sprite_x, sprite_y)

    pygame.display.update()
    fpsClock.tick(FPS)
