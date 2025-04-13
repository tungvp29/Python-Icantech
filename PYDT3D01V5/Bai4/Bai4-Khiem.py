#Yêu cầu:
#vẽ ra 4 mũi tên và đổi màu khi bấm các phím mũi tên tương ứng trên bàn phím
#khi ấn phím A thì đổi màu cả 4 mũi tên cùng lúc
#khi ấn phím Space thì đổi màu 4 mũi tên liên tục, ấn phím Space 1 lần nữa thì dừng đổi màu

import sys
import random
import pygame
pygame.init()
from pygame.locals import QUIT
Black=(0,0,0)
screen = pygame.display.set_mode((1000, 1000))
screen.fill(Black)
pygame.display.set_caption('Game')
UP=[255,255,255]
DOWN=[255,255,255]
RIGHT=[255,255,255]
LEFT=[255,255,255]
cach=0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
           pygame.quit()
           sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                for i in range(3):
                    del UP[0]
                    UP.append(random.randint(0,255))
            if event.key==pygame.K_DOWN:
                for i in range(3):
                    del DOWN[0]
                    DOWN.append(random.randint(0,255)) 
            if event.key==pygame.K_RIGHT:
                for i in range(3):
                    del RIGHT[0]
                    RIGHT.append(random.randint(0,255))
            if event.key==pygame.K_LEFT:
                for i in range(3):
                    del LEFT[0]
                    LEFT.append(random.randint(0,255))
            if event.key==pygame.K_a:
                for i in range(3):
                    del UP[0]
                    del DOWN[0]
                    del RIGHT[0]
                    del LEFT[0]
                    Number = random.randint(0,255)
                    UP.append(Number)
                    DOWN.append(Number)
                    LEFT.append(Number)
                    RIGHT.append(Number)
            if event.key==pygame.K_SPACE:
                if cach==0:
                    cach=1
                else:
                    cach=0
    
    pygame.display.update()