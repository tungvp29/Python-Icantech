import random

import pygame

screen_width = 400
screen_height = 400
player_size = 30
player_speed = 1
enemy_size = 15
enemy_speed = 0.2
enemy_count = 4
player_pos = [screen_width // 2, screen_height - player_size]
enemy_list = []
for i in range(enemy_count):
    enemy_pos = [random.randint(0, screen_width - enemy_size), random.randint(-100, 0)]
    enemy_list.append(enemy_pos)

pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Game đua xe!')
def draw_object():
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (player_pos[0], player_pos[1], player_size, player_size))
    for enemy_pos in enemy_list:
        pygame.draw.rect(screen, (255, 0, 0), (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
def upadate_enemy():
    for i in range(len(enemy_list)):
        if enemy_list[i][1] >= 0 and enemy_list[i][1] < screen_height:
            enemy_list[i][1] += enemy_speed
        else:
            enemy_list[i][0] = random.randint(0, screen_width - enemy_size)
            enemy_list[i][1] = random.randint(-100, 0)
def collision_detection():
    return any(detect_collision(player_pos, enemy_pos) for enemy_pos in enemy_list)

def detect_collision(obj1_pos, obj2_pos):
    obj1_x = obj1_pos[0]
    obj1_y = obj1_pos[1]
    obj2_x = obj2_pos[0]
    obj2_y = obj2_pos[1]
    if (obj1_x >= obj2_x and obj1_x < (obj2_x + enemy_size)) or (obj2_x >= obj1_x and obj2_x < (obj1_x + player_size)):
        if (obj1_y >= obj2_y and obj1_y < (obj2_y + enemy_size)) or (obj2_y >= obj1_y and obj2_y < (obj1_y + player_size)):
            return True
    return False


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < screen_width - player_size:
        player_pos[0] += player_speed
    return False
score = 0
game_over = False
while not game_over:
    game_over = handle_events()
    upadate_enemy()
    if collision_detection():
        game_over = True
    draw_object()
    score =+ 1
    font = pygame.font.Font(None, 36)
    text = font.render("Score:" + str(score), 1, (255, 255, 255))
    screen.blit(text, (15, 15))
    pygame.display.update()