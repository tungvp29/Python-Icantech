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
pygame.display.set_caption("Hello World")

font = pygame.font.SysFont("Arial", 50)         #1  font chữ: Arial, cỡ 50

font2 = pygame.font.SysFont("Arial", 50, True, False)   # in đậm, nghiêng

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)

    #chữ không chính giữa màn hình
    text = font.render("Noi dung in ra man hinh", True, RED)            #2
    screen.blit(text, (400, 300))                                           #3

    #chữ chính giữa màn hình
    text2 = font2.render("Noi dung in ra man hinh", True, BLUE)
    textRect = text2.get_rect()
    textRect.center = (400, 300)                                            
    screen.blit(text2, textRect)

    pygame.draw.circle(screen, RED, (400,300), 10)           
    pygame.display.update()