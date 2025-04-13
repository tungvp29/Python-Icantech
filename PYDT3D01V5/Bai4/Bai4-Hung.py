import pygame, sys, random
from pygame.locals import QUIT
pygame.init()
screen=pygame.display.set_mode((400,400))
pygame.draw.polygon(screen, (0,0,0), [(100, 100), (150, 50), (200, 100)])
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()