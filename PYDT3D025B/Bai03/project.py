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

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rắn săn mồi")

# Khởi tạo biến cho rắn
snake_block = 20
x_head = 400
y_head = 300

x_head_change = 0
y_head_change = 0

clock = pygame.time.Clock()

def randomFood():
    randFoodX = random.randrange(0, screen_width - snake_block)
    surplusFoodX = randFoodX % snake_block
    foodX = randFoodX - surplusFoodX
    randFoodY = random.randrange(0, screen_height - snake_block)
    surplusFoodY = randFoodY % snake_block
    foodY = randFoodY - surplusFoodY
    return foodX, foodY

foodX, foodY = randomFood()

snake_list = []
snake_length = 1
head_direction = 'left'

def show_snake(snake_list):
    for x in snake_list:
        if x == snake_list[-1]:
            pygame.draw.rect(screen, BLUE, (x[0], x[1], snake_block, snake_block))
            # head_skin = pygame.image.load(f'Graphics/head_{head_direction}.png').convert()
            # head_skin = pygame.transform.scale(head_skin, (snake_block, snake_block))
            # screen.blit(head_skin, (x[0], x[1]))
        else:
            pygame.draw.rect(screen, GREEN, (x[0], x[1], snake_block, snake_block))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and head_direction != 'right':
                x_head_change = -snake_block
                y_head_change = 0
                head_direction = 'left'
            elif event.key == pygame.K_RIGHT and head_direction != 'left':
                x_head_change = snake_block
                y_head_change = 0
                head_direction = 'right'
            elif event.key == pygame.K_UP and head_direction != 'down':
                x_head_change = 0
                y_head_change = -snake_block
                head_direction = 'up'
            elif event.key == pygame.K_DOWN and head_direction != 'up':
                x_head_change = 0
                y_head_change = snake_block
                head_direction = 'down'
            
    screen.fill(WHITE)
    # Vẽ rắn
    # pygame.draw.rect(screen, GREEN, (x_head, y_head, snake_block, snake_block))
    x_head += x_head_change
    y_head += y_head_change

    snake_head = []
    snake_head.append(x_head)
    snake_head.append(y_head)
    snake_list.append(snake_head)  # Thêm đầu rắn vào danh sách
    if len(snake_list) > snake_length:
        del snake_list[0]  # Xóa phần đuôi rắn nếu chiều dài lớn hơn

    show_snake(snake_list)    

    pygame.draw.rect(screen, RED, (foodX, foodY, snake_block, snake_block))  # Vẽ thức ăn
    # food_skin = pygame.image.load('Graphics/apple.png').convert()
    # food_skin = pygame.transform.scale(food_skin, (snake_block, snake_block))
    # screen.blit(food_skin, (foodX, foodY))
    
    # Kiểm tra va chạm với thức ăn
    if x_head == foodX and y_head == foodY:
        foodX, foodY = randomFood()
        snake_length += 1

    
    # font = pygame.font.Font (None, 36)
    # text = font.render("Score:"+ str(snake_length), 1, (0, 0, 0))
    # screen.blit(text, (10, 10)) 
    pygame.display.update()
    clock.tick(12)  # Tốc độ di chuyển của rắn