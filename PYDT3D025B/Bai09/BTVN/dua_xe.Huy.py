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
game_over = False
while not game_over:
    game_over = handle_event()
    update_enemy()
    draw_objects()
    pygame.display.update()

