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
pygame.display.set_caption("Arrow key control")

#vẽ các phím mũi tên
arrow_up = pygame.draw.polygon(screen, WHITE, [(400, 100), (380, 150), (420, 150)])
arrow_down = pygame.draw.polygon(screen, WHITE, [(400, 500), (380, 450), (420, 450)])
arrow_left = pygame.draw.polygon(screen, WHITE, [(200, 300), (250, 280), (250, 320)])
arrow_right = pygame.draw.polygon(screen, WHITE, [(600, 300), (550, 280), (550, 320)])

def randomColor():
    r = random.randint(0, 255)  #red
    g = random.randint(0, 255)  #green
    b = random.randint(0, 255)  #blue
    return (r, g, b)

clock = pygame.time.Clock()

is_changing = False #biến kiểm tra xem có đang tự động đổi màu hay không

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            #đổi màu khi ấn các phím mũi tên
            if event.key == pygame.K_UP:
                arrow_up = pygame.draw.polygon(screen, randomColor(), [(400, 100), (380, 150), (420, 150)])
            if event.key == pygame.K_DOWN:
                arrow_down = pygame.draw.polygon(screen, randomColor(), [(400, 500), (380, 450), (420, 450)])
            if event.key == pygame.K_LEFT:
                arrow_left = pygame.draw.polygon(screen, randomColor(), [(200, 300), (250, 280), (250, 320)])
            if event.key == pygame.K_RIGHT:
                arrow_right = pygame.draw.polygon(screen, randomColor(), [(600, 300), (550, 280), (550, 320)])
            #đổi màu cả 4 mũi tên khi ấn phím space
            if event.key == pygame.K_SPACE:
                arrow_up = pygame.draw.polygon(screen, randomColor(), [(400, 100), (380, 150), (420, 150)])
                arrow_down = pygame.draw.polygon(screen, randomColor(), [(400, 500), (380, 450), (420, 450)])
                arrow_left = pygame.draw.polygon(screen, randomColor(), [(200, 300), (250, 280), (250, 320)])
                arrow_right = pygame.draw.polygon(screen, randomColor(), [(600, 300), (550, 280), (550, 320)])
            #tự động đổi màu khi ấn phím enter, ấn enter lần nữa thì dừng lại
            if event.key == pygame.K_RETURN:
                is_changing = not is_changing
            #đổi màu nền khi ấn phím r, g, b
            if event.key == pygame.K_r:
                screen.fill(RED)
            if event.key == pygame.K_g:
                screen.fill(GREEN)
            if event.key == pygame.K_b:
                screen.fill(BLUE)
                
    if is_changing:
        arrow_up = pygame.draw.polygon(screen, randomColor(), [(400, 100), (380, 150), (420, 150)])
        arrow_down = pygame.draw.polygon(screen, randomColor(), [(400, 500), (380, 450), (420, 450)])
        arrow_left = pygame.draw.polygon(screen, randomColor(), [(200, 300), (250, 280), (250, 320)])
        arrow_right = pygame.draw.polygon(screen, randomColor(), [(600, 300), (550, 280), (550, 320)])
    
    pygame.display.update()
    # clock.tick(4)