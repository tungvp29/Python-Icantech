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
player_size = 50
player_speed = 1
enemy_size = 30
enemy_speed = 0.2
enemy_count = 5

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Racing Game")

player_pos = [screen_width // 2, screen_height - player_size]
enemy_list = []
for i in range(enemy_count):
    # enemy_x = random.randint(0, screen_width - enemy_size)
    # enemy_y = random.randint(-100, 0)
    # enemy_list.append([enemy_x, enemy_y])
    enemy_pos = [random.randint(0, screen_width - enemy_size), random.randint(-100, 0)]
    enemy_list.append(enemy_pos)

def draw_objects():
    screen.fill(BLACK)
    #Vẽ người chơi
    pygame.draw.rect(screen, WHITE, (player_pos[0], player_pos[1], player_size, player_size))
    #Vẽ kẻ địch
    for enemy in enemy_list:
        pygame.draw.rect(screen, RED, (enemy[0], enemy[1], enemy_size, enemy_size))

def update_enemy():
    for i in range(len(enemy_list)):
        if enemy_list[i][1] >= 0 and enemy_list[i][1] < screen_height:
            enemy_list[i][1] += enemy_speed
        else:
            enemy_list[i][0] = random.randint(0, screen_width - enemy_size)
            enemy_list[i][1] = random.randint(-100, 0)

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    
game_over = False
while not game_over:
    game_over = handle_events()

    update_enemy()

    draw_objects()

    pygame.display.update()