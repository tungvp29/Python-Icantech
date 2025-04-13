import pygame, sys, random

pygame.init()

screen_width = 800
screen_height = 600
player_size = 50
player_speed = 1
player_car = pygame.image.load("cars/car.png")
player_x, player_y = 360 / 5, 649 / 5
enemy_size = 30
enemy_speed = 0.2
enemy_count = 5

player_pos = [screen_width / 2, screen_height - 3 * player_size]
enemy_list = []
for i in range(enemy_count):
    enemy_pos = [random.randint(0, screen_width - enemy_size), random.randint(-100, 0)]
    enemy_list.append(enemy_pos)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Car Game")

def modify_image(image):
    return pygame.transform.scale(image, (player_x, player_y))

def draw_objects():
    screen.fill((255, 255, 255))
    player = pygame.Rect(player_pos[0], player_pos[1], player_size, player_size)
    # pygame.draw.rect(screen, (255, 0, 0), player)
    screen.blit(modify_image(player_car), (player_pos[0], player_pos[1]))
    for enemy_pos in enemy_list:
        enemy = pygame.Rect(enemy_pos[0], enemy_pos[1], enemy_size, enemy_size)
        pygame.draw.rect(screen, (0, 0, 0), enemy)

def event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def update():
    for enemy in enemy_list:
        enemy[1] += enemy_speed
        if enemy[1] > screen_height:
            enemy_pos = [random.randint(0, screen_width - enemy_size), random.randint(-100, 0)]
            enemy_list.remove(enemy)
            enemy_list.append(enemy_pos)

while True:
    event()
    draw_objects()
    update()
    pygame.display.update()