import pygame, random, sys
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (189, 203, 240)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
GRAY = (128, 128, 128)
BROWN = (139, 69, 19)

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Key arrow")
arrow_up = pygame.draw.polygon(screen, WHITE, [(400, 100), (380, 150), (420, 150)])
arrow_down = pygame.draw.polygon(screen, WHITE, [(400, 500), (380, 450), (420, 450)])
arrow_left = pygame.draw.polygon(screen, WHITE, [(200, 300), (250, 280), (250, 320)])
arrow_right = pygame.draw.polygon(screen, WHITE, [(600, 300), (550, 280), (550, 320)])
def RandomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)            #tuple

Clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            sys.quit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                arrow_up = pygame.draw.polygon(screen, RandomColor(), [(400, 100), (380, 150), (420, 150)])
            elif event.key == pygame.K_DOWN:
                arrow_down = pygame.draw.polygon(screen, RandomColor(), [(400, 500), (380, 450), (420, 450)])
            elif event.key == pygame.K_RIGHT:
                arrow_right = pygame.draw.polygon(screen, RandomColor(), [(600, 300), (550, 280), (550, 320)])
            elif event.key == pygame.K_LEFT:
                arrow_left = pygame.draw.polygon(screen, RandomColor(), [(200, 300), (250, 280), (250, 320)])
            elif event.key == pygame.K_SPACE:
                arrow_up = pygame.draw.polygon(screen, RandomColor(), [(400, 100), (380, 150), (420, 150)])
                arrow_down = pygame.draw.polygon(screen, RandomColor(), [(400, 500), (380, 450), (420, 450)])
                arrow_left = pygame.draw.polygon(screen, RandomColor(), [(200, 300), (250, 280), (250, 320)])
                arrow_right = pygame.draw.polygon(screen, RandomColor(), [(600, 300), (550, 280), (550, 320)])
    pygame.display.update()