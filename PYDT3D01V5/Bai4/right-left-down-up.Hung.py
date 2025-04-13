import pygame, sys, random, time as t 
from pygame.locals import QUIT
pygame.init()

screen = pygame.display.set_mode((400, 400))
color_up = (255, 0, 0)
color_down = (0, 255, 0)
color_left = (0, 0, 255)
color_right = (255, 255, 0)

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
auto_change = False 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                color_up = random_color() 
                color_down = random_color()
                color_left = random_color()
                color_right = random_color()
            if event.key == pygame.K_UP:
                color_up = random_color()  
            elif event.key == pygame.K_DOWN:
                color_down = random_color()
            elif event.key == pygame.K_LEFT:
                color_left = random_color()
            elif event.key == pygame.K_RIGHT:
                color_right = random_color()
            elif event.key == pygame.K_SPACE:  
                auto_change = not auto_change

    if auto_change:
        color_up = random_color()
        color_down = random_color()
        color_left = random_color()
        color_right = random_color()
        t.sleep(0.1)
    pygame.draw.polygon(screen, color_up, [(200, 50), (190, 100), (210, 100)])
    pygame.draw.polygon(screen, color_down, [(200, 350), (190, 300), (210, 300)])
    pygame.draw.polygon(screen, color_left, [(50, 200), (100, 190), (100, 210)])
    pygame.draw.polygon(screen, color_right, [(350, 200), (300, 190), (300, 210)])

    pygame.display.update()