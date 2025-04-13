import pygame, sys,random
from pygame.locals import QUIT
Screen_width = 800
Screen_hength = 600
screen = pygame.display.set_mode((Screen_width, Screen_hength))
player_side = 50
player_speed = 1
enemy_side = 30
enemy_speed = 0.2
enemy_count = 15
player_pos = [Screen_width/2, Screen_hength - player_side]
enemy= []
for i in range(enemy_count):
    enemy_pos = [random.randint(0, Screen_width - enemy_side), random.randint(-100,0)]
    enemy.append(enemy_pos) 
pygame.init() 
def draw_enemy():
    screen.fill((255,255,255))
    pygame.draw.rect(screen,(0,0,0),(player_pos[0],player_pos[1],player_side,player_side))
    for i in enemy:
        pygame.draw.rect(screen,(255,0,0),(i[0],i[1],enemy_side,enemy_side))
def update_enemy():
    for i in range(len(enemy)):
        if enemy[i] [1] >= 0 and enemy[i] [1] < Screen_hength: 
            enemy[i] [1] += enemy_speed
        else:
            enemy[i][0] = random.randint(0, Screen_width - enemy_side)
            enemy[i][1] = random.randint(-100,0)
def detect_collision(obj1_pos, obj2_pos):
    obj1_x = obj1_pos[0]
    obj1_y = obj1_pos[1]
    obj2_x = obj2_pos[0]
    obj2_y = obj2_pos[1]
    if (obj1_x >= obj2_x and obj1_x < (obj2_x + enemy_side)) or (obj2_x >= obj1_x and obj2_x < (obj1_x + player_side)):
        if (obj1_y >= obj2_y and obj1_y < (obj2_y + enemy_side))or (obj2_y >= obj1_y and obj2_y < (obj1_y + player_side)):
            return True 
    return False
def collision_detection():
    for enemy_pos in enemy:
        if detect_collision (player_pos, enemy_pos):
            return True
    return False

def event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             return True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0]>0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0]<Screen_width-player_side:
        player_pos[0] += player_speed
    return False

Game_over = False
while not Game_over:
    Game_over = event()
    draw_enemy()
    update_enemy()
    if collision_detection():
        Game_over=True
    pygame.display.update()