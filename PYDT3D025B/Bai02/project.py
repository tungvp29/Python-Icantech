import pygame, sys, random

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

# Khởi tạo biến cho rắn
snake_block = 20
x_head = 400
y_head = 300

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
                x_head_change = -20
                y_head_change = 0
            elif event.key == pygame.K_RIGHT:
                x_head_change = 20
                y_head_change = 0
            elif event.key == pygame.K_UP:
                x_head_change = 0
                y_head_change = -20
            elif event.key == pygame.K_DOWN:
                x_head_change = 0
                y_head_change = 20
            
    screen.fill(WHITE)
    # Vẽ rắn
    pygame.draw.rect(screen, GREEN, (x_head, y_head, snake_block, snake_block))
    x_head += x_head_change
    y_head += y_head_change

    # pygame.draw.rect(screen, RED, (random.randint(0, 800), random.randint(0, 600), snake_block, snake_block))  # Vẽ thức ăn

    pygame.display.update()
    clock.tick(12)  # Tốc độ di chuyển của rắn