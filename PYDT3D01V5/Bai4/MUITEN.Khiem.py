#Yêu cầu:
#vẽ ra 4 mũi tên và đổi màu khi bấm các phím mũi tên tương ứng trên bàn phím
#khi ấn phím A (ALL) thì đổi màu cả 4 mũi tên cùng lúc
#khi ấn phím Space thì đổi màu 4 mũi tên liên tục, ấn phím Space 1 lần nữa thì dừng đổi màu

import sys
import random
import pygame
pygame.init()
from pygame.locals import QUIT
Black=(0,0,0)
WHITE=(255,255,255)
screen = pygame.display.set_mode((500,500))
screen.fill(Black)
pygame.display.set_caption('Game')
UP=[255,255,255]
DOWN=[255,255,255]
RIGHT=[255,255,255]
LEFT=[255,255,255]
cach=0
clock=pygame.time.Clock()
def Random():
    a=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    return a
while True:
    clock.tick(12)
    for event in pygame.event.get():
        if event.type == QUIT:
           pygame.quit()
           sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                    UP = Random()
            elif event.key==pygame.K_DOWN:
                    DOWN = Random()
            elif event.key==pygame.K_RIGHT:
                    RIGHT = Random()
            elif event.key==pygame.K_LEFT:
                    LEFT = Random()
            elif event.key==pygame.K_a:
                    UP = Random()
                    DOWN = Random()
                    LEFT = Random()
                    RIGHT = Random()
            elif event.key==pygame.K_SPACE:
                if cach==0:
                    cach=1
                else:
                    cach=0
    if cach==1:
                    UP = Random()
                    DOWN = Random()
                    LEFT = Random()
                    RIGHT = Random()
    pygame.draw.polygon(screen, UP, [(200, 50), (190, 100), (210, 100)])
    pygame.draw.polygon(screen, DOWN, [(200, 350), (190, 300), (210, 300)])
    pygame.draw.polygon(screen, LEFT , [(50, 200), (100, 190), (100, 210)])
    pygame.draw.polygon(screen, RIGHT , [(350, 200), (300, 190), (300, 210)])
    pygame.display.update()