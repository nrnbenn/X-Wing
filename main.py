import pygame
from pygame.locals import *

def update():
    pygame.display.update()

#pygame setup
size = width, height = (1000, 1000)
pygame.init()
running = True
screen = pygame.display.set_mode(size)
pygame.display.set_caption("X-Wing")
update()


#loop
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

pygame.quit()


#replit commit test
