import pygame, sys, random
from pygame.locals import QUIT

#Khai báo các màu thường dùng
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEEN = (0, 255, 0)
BLUE = (50, 153, 213)

pygame.init()
font = pygame.font.SysFont('Tahoma', 20)

#Kích thước màn hình và nội dung tiêu đề
screen_width = 600
screen_height = 400
title = 'Ran san moi'
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(title)

#Thông số khởi tạo của rắn
snake_block = 10
x_head = 300
y_head = 200
x_head_change = 0
y_head_change = 0

clock = pygame.time.Clock()

#Tạo con mồi ngẫu nhiên
randFoodX = random.randrange(0, screen_width - 10)
surplusFoodX = randFoodX % 10
foodX = round(randFoodX - surplusFoodX)
randFoodY = random.randrange(0, screen_height - 10)
surplusFoodY = randFoodY % 10
foodY = round(randFoodY - surplusFoodY)

snake_list = []
snake_length = 1

#Vẽ rắn
def ShowSnake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, BLUE, [x[0], x[1], snake_block, snake_block])

def Message(msg, color):
    mesg = font.render(msg, True, color)
    mesgRect = mesg.get_rect()
    mesgRect.center = (screen_width/2, screen_height/2)
    screen.blit(mesg, mesgRect)
    
def ShowScore(score):
    value = font.render('Điểm số: ' + str(score), True, BLACK)
    screen.blit(value, [0,0])

gameClose = False
isStarted = False
isPaused = False
while True:
    while gameClose == True:
        screen.fill(WHITE)
        Message('Bạn đã thua, nhấn phím Space để chơi lại hoặc phím ESC để thoát', RED)
        ShowScore(snake_length - 1)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    x_head = 300
                    y_head = 200
                    x_head_change = 0
                    y_head_change = 0
                    snake_list = []
                    snake_length = 1
                    gameClose = False
                    isStarted = False
                    isPaused = False
    #Xử lý các sự kiến bấm phím
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_head_change = -10
                y_head_change = 0
            elif event.key == pygame.K_RIGHT:
                x_head_change = 10
                y_head_change = 0
            elif event.key == pygame.K_UP:
                x_head_change = 0
                y_head_change = -10
            elif event.key == pygame.K_DOWN:
                x_head_change = 0
                y_head_change = 10
            elif event.key == pygame.K_SPACE:
                isStarted = not isStarted

    if not isStarted:
        screen.fill(BLUE)
        text = font.render('Nhấn phím Space để bắt đầu', True, WHITE)
        textRect = text.get_rect()
        textRect.center = (screen_width//2, screen_height//2)
        screen.blit(text, textRect)
    else:
        screen.fill(WHITE)

        #Vẽ con mồi ngẫu nhiên
        pygame.draw.rect(screen, RED, [foodX, foodY, snake_block, snake_block])
        #Cập nhật vị trí con rắn dựa trên phím bấm
        #pygame.draw.rect(screen, BLUE, [x_head,y_head,snake_block,snake_block])
        x_head += x_head_change
        y_head += y_head_change

        snake_head = []  #[x, y] của đầu con rắn
        snake_head.append(x_head)
        snake_head.append(y_head)
        #thêm tọa độ đầu rắn vào danh sách tất cả các khúc của con rắn
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
        ShowSnake(snake_block, snake_list)
        #kiểm tra rắn chạm mồi
        if x_head == foodX and y_head == foodY:
            randFoodX = random.randrange(0, screen_width - 10)
            surplusFoodX = randFoodX % 10
            foodX = round(randFoodX - surplusFoodX)
            randFoodY = random.randrange(0, screen_height - 10)
            surplusFoodY = randFoodY % 10
            foodY = round(randFoodY - surplusFoodY)
            snake_length += 1

        #Kiểm tra rắn chạm tường
        if x_head >= screen_width or x_head < 0 or y_head >= screen_height or y_head < 0:
            gameClose = True

        #Kiểm tra rắn chạm chính nó
        for x in snake_list[:-1]:
            if x == snake_head:
                gameClose = True
        ShowScore(snake_length - 1)
    pygame.display.update()
    clock.tick(12)
