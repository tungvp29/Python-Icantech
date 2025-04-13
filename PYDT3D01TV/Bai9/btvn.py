import pygame, sys, random

pygame.init()
screenWidth = 800
screenHeight = 600
playerSize = 50
playerSpeed = 1
playerPos = [screenWidth/2, screenHeight-2*playerSize]

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('BTVN')

def DrawObject():
    screen.fill((255,255,255))
    pygame.draw.rect(screen, (0,0,0), (playerPos[0], playerPos[1], playerSize, playerSize))

def HandleEvents():
    #Sựn kiện thoát game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    #Xử lý sự kiện phím bấm
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and playerPos[0] > 0:
        playerPos[0] -= playerSpeed
    if keys[pygame.K_RIGHT] and playerPos[0] < screenWidth - playerSize:
        playerPos[0] += playerSpeed
    if keys[pygame.K_UP] and playerPos[1] > 0:
        playerPos[1] -= playerSpeed
    if keys[pygame.K_DOWN] and playerPos[1] < screenHeight - playerSize:
        playerPos[1] += playerSpeed
    return False

while True:
    
    HandleEvents()
    DrawObject()

    pygame.display.update()