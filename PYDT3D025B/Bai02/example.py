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
pygame.display.set_caption("Rắn săn mồi")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Phím trái được nhấn")
            elif event.key == pygame.K_RIGHT:
                print("Phím phải được nhấn")
            elif event.key == pygame.K_UP:
                print("Phím lên được nhấn")
            elif event.key == pygame.K_DOWN:
                print("Phím xuống được nhấn")
            