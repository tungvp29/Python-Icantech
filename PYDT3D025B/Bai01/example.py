import pygame, sys

pygame.init()

screen = pygame.display.set_mode((1024, 800)) #kích thước cửa sổ
pygame.display.set_caption("Hello World")

#color
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
GRAY = (128, 128, 128)

# screen.fill(BLUE) #đổ màu đỏ cho cửa sổ
# đặt câu lệnh vẽ ở đây
screen.fill(WHITE)

pygame.draw.rect(screen, RED, (100, 100, 250, 250), 10) #vẽ hình chữ nhật màu đỏ
pygame.draw.rect(screen, GREEN, (350, 350, 100, 200)) 
pygame.draw.ellipse(screen, CYAN, (350, 350, 100, 200)) 

pygame.draw.circle(screen, BLUE, (200, 200), 50, 1) #vẽ hình tròn màu xanh

pygame.draw.polygon(screen, YELLOW, [(300, 300), (400, 400), (500, 300), (400, 200)]) #vẽ hình đa giác màu vàng
pygame.draw.lines(screen, GRAY, True, [(300, 300), (400, 400), (500, 300), (400, 200)], 10) #vẽ đường thẳng màu đỏ
pygame.draw.line(screen, GRAY, (300, 300), (400, 400), 10) #vẽ đường thẳng màu đỏ

pygame.display.update()
# đặt câu lệnh vẽ sau update
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()