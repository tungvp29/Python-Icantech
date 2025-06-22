import pygame, random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SIZE = 50
PLAYER_SPEED = 1
ENEMY_SIZE = 10
ENEMY_SPEED = 3
ENEMY_COUNT = 0
player_pos = [SCREEN_WIDTH/2, SCREEN_HEIGHT-PLAYER_SIZE]
enemy_list = []
for i in range(ENEMY_COUNT):
    enemy_pos = [random.randint(0,SCREEN_WIDTH - ENEMY_SIZE),random.randint(-100, 0)]
    enemy_list.append(enemy_pos)
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("skibidi") 
def draw_object():
    screen.fill((0,0,0))
    for enemy_pos in enemy_list:
        screen.blit(enemy_car,(enemy_pos[0],enemy_pos[1]-ENEMY_SIZE))
    screen.blit(player_car, (player_pos[0], player_pos[1]- PLAYER_SIZE))




def update_enemy():
    for i in range(len(enemy_list)):
        if enemy_list[i][1] >= 0 and enemy_list[i][1] < SCREEN_HEIGHT:
            enemy_list[i][1] += ENEMY_SPEED
        else:
            enemy_list[i][0] = random.randint(0,SCREEN_WIDTH - ENEMY_SIZE)
            enemy_list[i][1] = random.randint(-100,0)
player_car = pygame.image.load("mr beast/car-blue.png")
enemy_car = pygame.image.load("mr beast/car-red.png")
player_car = pygame.transform.flip(player_car,False,True)
clock = pygame.time.Clock()
def collision_detection():
    for enemy_pos in enemy_list:
        if detect_collision(player_pos,enemy_pos):
            return True
    return False



def detect_collision(player_pos,enemy_pos):
    player_posx = player_pos[0]
    player_posy = player_pos[1]
    enemy_posx = enemy_pos[0]
    enemy_posy = enemy_pos[1]
    if (player_posx >= enemy_posx and player_posx < (enemy_posx + ENEMY_SIZE)) or (enemy_posx >= player_posx and enemy_posx < (player_posx + PLAYER_SIZE)):
        if (player_posy >= enemy_posy and player_posy < (enemy_posy + ENEMY_SIZE)) or (enemy_posy >= player_posy) and enemy_posy < (player_posy + PLAYER_SIZE):
            return True
    return False

def handle_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= PLAYER_SPEED
    if keys[pygame.K_RIGHT] and player_pos[0] < SCREEN_WIDTH - PLAYER_SIZE:
        player_pos[0] += PLAYER_SPEED
    return False
score = 0

game_over = False
while not game_over:
    game_over = handle_event()

    update_enemy()
    if collision_detection():
        game_over = True
    
    draw_object()
    score += 1
    font = pygame.font.Font(None, 36)
    text = font.render("Score:" + str(score), 1,(255,255,255))
    screen.blit(text,(10,10))
    
    
    
    pygame.display.update()
    clock.tick(10000000000000000000000000000000000000000000000000000000000000000000000000000000)