import pygame, sys

pygame.init()
#color
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (189, 203, 240)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
GRAY = (128, 128, 128)
BROWN = (139, 69, 19)

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Họa sĩ tài năng")

sunPosY = 100
direction = 1
r = 255

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)

    # đặt câu lệnh vẽ ở đây 
    #nền nhà
    pygame.draw.rect(screen, BROWN, (0, 500, 800, 100))
    #tường nhà
    pygame.draw.rect(screen, RED, (250, 250, 300, 250))
    #MÁI NHÀ
    pygame.draw.polygon(screen, GREEN, [(400, 100), (100, 250), (700, 250)])
    #mặt trời
    pygame.draw.circle(screen, (r, 255, 0), (700, sunPosY), 50)
    r += 1
    if r >= 255:
        r = 0
    
    if sunPosY >= 100:
        direction = -0.2
    elif sunPosY <= -70:
        direction = 0.2
    sunPosY += direction

    #hoa
    pygame.draw.line(screen, GREEN, (100, 500), (100, 550), 10)
    pygame.draw.circle(screen, YELLOW, (100, 480), 20, 5)
    pygame.draw.circle(screen, RED, (100, 480), 10)
    
    #mây
    pygame.draw.circle(screen, CYAN, (200, 100), 30)
    pygame.draw.circle(screen, CYAN, (250, 100), 30)
    pygame.draw.circle(screen, CYAN, (225, 80), 30)
    pygame.draw.circle(screen, CYAN, (300, 100), 30)
    pygame.draw.circle(screen, CYAN, (350, 100), 30)
    pygame.draw.circle(screen, CYAN, (325, 80), 30)
    pygame.draw.circle(screen, CYAN, (400, 100), 30)
    pygame.draw.circle(screen, CYAN, (450, 100), 30)

    #move the clouds
    pygame.display.update()