import pygame, sys, random

pygame.init()

# Screen and player settings
screen_width = 800
screen_height = 600
player_size_x = 50
player_size_y = 90
player_speed = 1
player_car = pygame.image.load("cars/car.png")
player_x, player_y = 360 / 5, 649 / 5

# Enemy settings
enemy_size_x = 50
enemy_size_y = 90
enemy_speed = 0.5
enemy_count = 5
enemy_car = pygame.image.load('cars/car2.png')

# Position and list of enemies
player_pos = [screen_width / 2, screen_height - 2 * player_size_y]
enemy_list = []
for i in range(enemy_count):
    enemy_pos = [random.randint(0, screen_width - enemy_size_x), random.randint(-100, 0)]
    enemy_list.append(enemy_pos)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Car Game")

# Score, game over flag, and font
score = 0
game_over = False
font = pygame.font.Font(None, 35)

def draw_objects():
    screen.fill((255, 255, 255))
    screen.blit((player_car), (player_pos[0], player_pos[1]))
    for enemy_pos in enemy_list:
        screen.blit((enemy_car), (enemy_pos[0], enemy_pos[1]))

def display_score():
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

def game_over_screen():
    game_over_text = font.render(f"Game Over! Final Score: {score}", True, (255, 0, 0))
    screen.blit(game_over_text, (screen_width / 4, screen_height / 2))
    pygame.display.update()
    pygame.time.delay(1000)

def restart_screen():
    restart_txt = font.render("Press Enter to restart or close to exit", True, (0, 0, 0))
    screen.blit(restart_txt, (screen_width / 4, screen_height / 2 + 50))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # Ensure the game exits
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return True  # Break out of the loop and rest

def event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if key[pygame.K_RIGHT] and player_pos[0] < screen_width - player_size_x:
        player_pos[0] += player_speed

def detect(player_pos, enemy_pos):
    player_pos_x = player_pos[0]
    player_pos_y = player_pos[1]
    enemy_pos_x = enemy_pos[0]
    enemy_pos_y = enemy_pos[1]
    if (player_pos_x >= enemy_pos_x and player_pos_x <= enemy_pos_x + enemy_size_x) or (enemy_pos_x >= player_pos_x and enemy_pos_x <= player_pos_x + player_size_x):
        if (player_pos_y >= enemy_pos_y and player_pos_y <= enemy_pos_y + enemy_size_y) or (enemy_pos_y >= player_pos_y and enemy_pos_y <= player_pos_y + player_size_y):
            return True
    return False

def state():
    for enemy_pos in enemy_list:
        if detect(player_pos, enemy_pos):
            return True
    return False

def update():
    global score, enemy_speed
    for enemy in enemy_list:
        enemy[1] += enemy_speed
        if enemy[1] > screen_height:
            enemy_pos = [random.randint(0, screen_width - enemy_size_x), random.randint(-100, 0)]
            enemy_list.remove(enemy)
            enemy_list.append(enemy_pos)

    if score % 1000 == 0 and score != 0:
        enemy_speed += 0.1

while True:
    if not game_over:
        event()
        draw_objects()
        display_score()

        if state():
            game_over_screen()
            game_over = True  # Trigger the game over state

        update()
        score += 1
        pygame.display.update()
    else:
        restart_screen()
        # Reset game state after restart
        score = 0
        enemy_speed = 0.5
        player_pos = [screen_width / 2 - player_size_x / 2, screen_height - player_size_y - 10]
        enemy_list.clear()
        for i in range(enemy_count):
            enemy_pos = [random.randint(0, screen_width - enemy_size_x), random.randint(-100, 0)]
            enemy_list.append(enemy_pos)
        game_over = False  # Exit game-over state and resume game
 