import pygame, sys,random, os
from pygame.locals import QUIT
Screen_width = 800
Screen_hength = 600
screen = pygame.display.set_mode((Screen_width, Screen_hength))
def get_asset_path(filename):
    if hasattr(sys, '_MEIPASS'):
        # Running in a PyInstaller bundle
        return os.path.join(sys._MEIPASS, 'assets', filename)
    else:
        # Running in a development environment
        return os.path.join('assets', filename)
    
player_skin = pygame.image.load(get_asset_path("car.png")).convert()
player_skin = pygame.transform.rotate(player_skin,180)
enemy_skin =  pygame.image.load(get_asset_path("redCar.png")).convert()
player_size_x = 30
player_size_y = 50 
player_speed = 1
enemy_size_x = 30
enemy_size_y = 50
enemy_speed = 1.5
enemy_count = 20
player_skin = pygame.transform.scale(player_skin,(player_size_x, player_size_y))
enemy_skin = pygame.transform.scale(enemy_skin,(enemy_size_x,enemy_size_y))
player_pos = [Screen_width/2, Screen_hength - 50]
enemy= []
for i in range(enemy_count):
    enemy_pos = [random.randint(0, Screen_width - enemy_size_x), random.randint(-150,0)]
    enemy.append(enemy_pos) 
pygame.init() 
def draw_enemy():
    screen.fill((255,255,255))
    screen.blit(player_skin,(player_pos[0],player_pos[1]))
    for i in enemy:
        screen.blit(enemy_skin,(i[0],i[1]))
def update_enemy():
    for i in range(len(enemy)):
        if enemy[i] [1] >= 0 and enemy[i] [1] < Screen_hength: 
            enemy[i] [1] += enemy_speed
        else:
            enemy[i][0] = random.randint(0, Screen_width - enemy_size_x)
            enemy[i][1] = random.randint(-150,0)
def detect_collision(obj1_pos, obj2_pos):
    obj1_x = obj1_pos[0]
    obj1_y = obj1_pos[1]
    obj2_x = obj2_pos[0]
    obj2_y = obj2_pos[1]
    if (obj1_x >= obj2_x and obj1_x < (obj2_x + enemy_size_x)) or (obj2_x >= obj1_x and obj2_x < (obj1_x + player_size_x)):
        if (obj1_y >= obj2_y and obj1_y < (obj2_y + enemy_size_y))or (obj2_y >= obj1_y and obj2_y < (obj1_y + player_size_y)):
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
    if keys[pygame.K_RIGHT] and player_pos[0]<Screen_width-50:
        player_pos[0] += player_speed
    return False
score = 0
Game_over = False
while not Game_over:
    score +=1
    Game_over = event()
    draw_enemy()
    update_enemy()
    if collision_detection():
        Game_over=True
        print(score)
    font = pygame.font.Font (None, 36)
    text = font.render("Score:"+ str(score), 1, (0, 0, 0))
    screen.blit(text, (10, 10)) 
    pygame.display.update()