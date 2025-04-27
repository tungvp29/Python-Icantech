import pygame, sys, random
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
GRAY = (128, 128, 128)
pygame.init()
screen_width = 600
screen_height = 400
title = 'Ran san moi'
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(title)

snake_block = 10

x_head = 300
y_head = 200

x_head_change = 0
y_head_change = 0

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_head_change = -10
                y_head_change = 0
            if event.key == pygame.K_RIGHT:
                x_head_change = 10
                y_head_change = 0
            if event.key == pygame.K_UP:
                x_head_change = 0
                y_head_change = -10
            if event.key == pygame.K_DOWN:
                x_head_change = 0
                y_head_change = 10
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, [x_head, y_head, snake_block, snake_block])
    x_head += x_head_change
    y_head += y_head_change

    pygame.display.update()
    clock.tick(24)
    