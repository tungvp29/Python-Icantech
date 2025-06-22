import pygame, random
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SIZE = 50
PLAYER_SPEED = 1
ENEMY_SIZE = 30
ENEMY_SPEED = 0.25
ENEMY_COUNT = 5

player_pos = [SCREEN_WIDTH/2, SCREEN_HEIGHT - PLAYER_SIZE]
enemy_list = []
for i in range(ENEMY_COUNT):
    enemy_pos = [random.randint(0, SCREEN_WIDTH - ENEMY_SIZE), random.randint(-100, 0)]
    enemy_list.append(enemy_pos)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game racing")
def draw_objects():
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (player_pos[0], player_pos[1], ENEMY_SIZE, ENEMY_SIZE))
    for enemy_pos in enemy_list:
        pygame.draw.rect(screen, (255, 0, 0), (enemy_pos[0], enemy_pos[1], ENEMY_SIZE, ENEMY_SIZE))
def update_enemy():
    for i in range(len(enemy_list)):
        if enemy_list[i][1] >= 0 and enemy_list[i][1] < SCREEN_HEIGHT:
            enemy_list[i][1] += ENEMY_SPEED
        else:
            enemy_list[i][0] = random.randint(0, SCREEN_WIDTH - ENEMY_SIZE)
            enemy_list[i][1] = random.randint(-100, 0)
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
def detect_collision(obj1_pos, obj2_pos):
    obj1_x = obj1_pos[0]
    obj1_y = obj1_pos[1]
    obj2_x = obj2_pos[0]
    obj2_y = obj2_pos[1]
    if (obj1_x >= obj2_x and obj1_x < (obj2_x + ENEMY_SIZE)) or (obj2_x >= obj1_x and obj2_x < (obj1_x + PLAYER_SIZE)):
        if (obj1_y >= obj2_y and obj1_y < (obj2_y + ENEMY_SIZE)) or (obj2_y >= obj1_y and obj2_y < (obj1_y + PLAYER_SIZE)):
            return True
    return False
def collision_detection():
    for enemy_pos in enemy_list:
        if detect_collision(player_pos, enemy_pos):
            return True
    return False
score = 0
game_over = False
while not game_over:
    game_over = handle_event()
    update_enemy()
    if collision_detection():
        game_over = True
    draw_objects()
    score += 1
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score // 10), 1, (255, 255, 255))
    screen.blit(text, (10, 10))
    pygame.display.update()

