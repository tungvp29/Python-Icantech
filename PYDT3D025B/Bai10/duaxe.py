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
BLACK = (0, 0, 0)

screen_width = 800
screen_height = 600
player_size_x = 50
player_size_y = 90
player_speed = 1
enemy_size_x = 50
enemy_size_y = 90
enemy_speed = 0.2
enemy_count = 5
player_car = pygame.image.load("assets/car-blue.png")
player_car = pygame.transform.flip(player_car, False, True)
enemy_car = pygame.image.load("assets/car-red.png")
clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Racing Game")

player_pos = [screen_width // 2, screen_height - player_size_y]
enemy_list = []
for i in range(enemy_count):
    # enemy_x = random.randint(0, screen_width - enemy_size)
    # enemy_y = random.randint(-100, 0)
    # enemy_list.append([enemy_x, enemy_y])
    enemy_pos = [random.randint(0, screen_width - enemy_size_x), random.randint(-100, 0)]
    enemy_list.append(enemy_pos)

def draw_objects():
    screen.fill(BLACK)
    #Vẽ người chơi
    screen.blit(player_car, (player_pos[0], player_pos[1]))
    # pygame.draw.rect(screen, WHITE, (player_pos[0], player_pos[1], player_size_x, player_size_y))
    #Vẽ kẻ địch
    for enemy in enemy_list:
        screen.blit(enemy_car, (enemy[0], enemy[1]))
        # pygame.draw.rect(screen, RED, (enemy[0], enemy[1], enemy_size_x, enemy_size_y))

def update_enemy():
    for i in range(len(enemy_list)):
        if enemy_list[i][1] >= 0 and enemy_list[i][1] < screen_height:
            enemy_list[i][1] += enemy_speed
        else:
            enemy_list[i][0] = random.randint(0, screen_width - enemy_size_x)
            enemy_list[i][1] = random.randint(-100, 0)

def collision_detection():
    for enemy in enemy_list:
        if detect_collision(player_pos, enemy):
            return True
    return False

def detect_collision(player_pos, enemy_pos):
    playerPos_x = player_pos[0]
    playerPos_y = player_pos[1]
    enemyPos_x = enemy_pos[0]
    enemyPos_y = enemy_pos[1]
    if (playerPos_x >= enemyPos_x and playerPos_x < enemyPos_x + enemy_size_x) or (enemyPos_x >= playerPos_x and enemyPos_x < playerPos_x + player_size_x):
        if (playerPos_y >= enemyPos_y and playerPos_y < enemyPos_y + enemy_size_y) or (enemyPos_y >= playerPos_y and enemyPos_y < playerPos_y + player_size_y):
            return True
    return False

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and player_pos[0] < screen_width - player_size_x:
        player_pos[0] += player_speed
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed

game_over = False
score = 0
while not game_over:
    game_over = handle_events()

    update_enemy()

    draw_objects()

    score += 1
    if score % 1000 == 0 and score != 0:
        enemy_speed += 0.1

    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score//10}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    if collision_detection():        
        game_over = True

    pygame.display.update()
else:    
    screen.fill((255,255,255))
    font = pygame.font.Font(None, 72)
    text = font.render(f"Game Over", True, (0,0,0))
    screen.blit(text, (screen_width//2 - 150, screen_height//2 - 50))
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score//10}", True, (0,0,0))
    screen.blit(text, (screen_width//2 - 50, screen_height//2))
    pygame.display.update()
    pygame.time.wait(3000)