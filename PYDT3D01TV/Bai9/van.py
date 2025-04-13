import pygame, os, sys
import random

screen_width = 800
screen_height = 600
player_size = 50
player_speed = 1
enemy_size = 30
enemy_speed = 0.2
enemy_count = 5

# Khai báo biến 
player_pos = [screen_width / 2, screen_height - player_size]
enemy_list = []
for i in range(enemy_count):
    enemy_pos = [random.randint(0, screen_width - enemy_size), random.randint(-100, 0)]
    enemy_list.append(enemy_pos)

# Khởi tạo Pygame
pygame.init()

# Tạo màn hình game
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game đua xe")

font1 = pygame.font.SysFont("arial", 36)
text1 = font1.render("Game Over", True, (255, 255, 255))
screen.blit(text1, (0 , 0))

#Hàm lấy đường dẫn tới file hình ảnh
def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Tải và thu nhỏ hình ảnh xe
player_image = pygame.image.load(resource_path("player.png"))
player_image = pygame.transform.scale(player_image, (player_size, player_size))
enemy_image = pygame.image.load(resource_path("enemy.png"))
enemy_image = pygame.transform.scale(enemy_image, (enemy_size, enemy_size))

# Hàm vẽ đối tượng trên màn hình 
def draw_objects():
    screen.fill((0, 0, 0))
    screen.blit(player_image, (player_pos[0], player_pos[1]))
    for enemy_pos in enemy_list:
        screen.blit(enemy_image, (enemy_pos[0], enemy_pos[1]))

# Hàm để cập nhật vị trí của kẻ thù 
def update_enemy():
    for i in range(len(enemy_list)):
        if enemy_list[i][1] >= 0 and enemy_list[i][1] < screen_height:
            enemy_list[i][1] += enemy_speed
        else:
            enemy_list[i][0] = random.randint(0, screen_width - enemy_size)
            enemy_list[i][1] = random.randint(-100, 0)

def collsision_decetion():
    for enemy_pos in enemy_list:
        if detect_collision(player_pos, enemy_pos):
            return True
    return False

def detect_collision(player_pos, enemy_pos):
    player_x = player_pos[0]
    player_y = player_pos[1]
    enemy_x = enemy_pos[0]
    enemy_y = enemy_pos[0]
    if (player_x >= enemy_x and player_x < (enemy_x + enemy_size)) or  (enemy_x >= player_x and enemy_x < (player_x + player_size)):
        if (player_y >= enemy_y and player_y < ( enemy_y + enemy_size)) or (enemy_y >= player_y and enemy_y < (player_y + player_size)):
            return True

    
    return False

# Hàm xử lý sự kiện Đua xe
def handle_events():
    # Xử lý sự kiện thoát game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    return False

# Hàm điều khiển xe
def move_player():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < screen_width - player_size:
        player_pos[0] += player_speed
    if keys[pygame.K_UP] and player_pos[1] > 0:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN] and player_pos[1] < screen_height - player_size:
        player_pos[1] += player_speed
score = 0 

pygame.sound.load(resource_path("background.mp3"))
# Vòng lặp chính của game
game_over = False
while not game_over:
    # Xử lý sự kiện trong game 
    game_over = handle_events()

    # Điều khiển xe
    move_player()

    # Cập nhật vị trí của kẻ thù 
    update_enemy()

    if collsision_decetion():
        game_over = True

    # Vẽ các đối tượng trên màn hình 
    draw_objects()

    # Cập nhập điểm
    score += 1

    # Hiển thị điểm số trên màn hình 
    font = pygame.font.Font(None, 36)
    text = font.render("Điểm:" + str(score), 1, (255, 255, 255))
    
    

    # Cập nhật màn hình
    pygame.display.update()
