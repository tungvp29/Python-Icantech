import sys, pygame,random
from pygame import QUIT
Screen_width = 800
Screen_hength = 600
pygame.init()
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
def exit():
    for event in pygame.event.get():
         if event.type == QUIT:
             pygame.quit()
             sys.exit()
while True:
    exit()
    draw_enemy()
    update_enemy()
    pygame.display.update()