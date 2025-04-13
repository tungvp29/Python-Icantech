import random
import sys

import pygame
from pygame.locals import QUIT

screen_width = 400
screen_height = 400
player_size = 20
player_speed = 2
enemy_size = 20
enemy_speed = 0.2
enemy_count = 5
player_pos = [screen_width // 2, screen_height - player_size]
enemy_list = []
for i in range(enemy_count):
    enemy_pos = [random.randint(0, screen_width - enemy_size), random.randint(-100, 0)]
    enemy_list.append(enemy_pos)
    
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Game đua xe!')
def draw_object():
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (player_pos[0], player_pos[1], player_size, player_size))
    for enemy_pos in enemy_list:
        pygame.draw.rect(screen, (255, 0, 255), (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
def upadate_enemy():
    for i in range(len(enemy_list)):
        if enemy_list[i][1] >= 0 and enemy_list[i][1] < screen_height:
            enemy_list[i][1] += enemy_speed
        else:
            enemy_list[i][0] = random.randint(0, screen_width - enemy_size)
            enemy_list[i][1] = random.randint(-100, 0)
def handle_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
game_over = False
while not game_over:
    game_over = handle_event()
    upadate_enemy()
    draw_object()
    pygame.display.update()