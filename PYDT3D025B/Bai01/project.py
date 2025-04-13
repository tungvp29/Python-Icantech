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
    pygame.draw.circle(screen, YELLOW, (700, sunPosY), 50)
    sunPosY -= 1
    if sunPosY < -50:
        sunPosY = 100

    pygame.display.update()