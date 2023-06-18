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

#game setup
#create list of ships to be assigned
ships = team1, team2 = (),()
team1 = ("TieFighter","TieFighter")
team2 = ("X-Wing")

#create ship class
class ship():
    def __init__(self):
        pass

    
#MAIN
#load board
board = pygame.image.load("images/boards/board.png")
boardloc = board.get_rect()
boardloc.topleft = 0,0

#print board
screen.blit(board,boardloc)
update()



#loop
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

pygame.quit()
