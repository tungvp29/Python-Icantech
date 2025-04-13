import pygame
import random
import os
import sys

# Khởi tạo Pygame
pygame.init()

# Thiết lập màn hình
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Lật Hình")

# Khởi tạo font
font = pygame.font.SysFont(None, 40)

# Màu sắc
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Kích thước lưới và gạch
GRID_WIDTH = 4  # Số ô ngang
GRID_HEIGHT = 3  # Số ô dọc
TILE_SIZE = 150  # Kích thước ô

# Tải âm thanh
pygame.mixer.music.load("a.mp3")
pygame.mixer.music.play(-1)  # Phát nhạc nền

# Hàm thu nhỏ hình ảnh
def resize_image(image, size):
    return pygame.transform.scale(image, size)

# Danh sách hình ảnh - Giả định đã có 5 cặp hình ảnh trong thư mục "images"
images = []
image_folder = "images"
image_filenames = [
    "image1.png", "image1.png", 
    "image2.png", "image2.png", 
    "image3.png", "image3.png", 
    "image4.png", "image4.png", 
    "image5.png", "image5.png",
    "image6.png", "image6.png"
]

# Tải và thu nhỏ hình ảnh
for filename in image_filenames:
    try:
        image_path = os.path.join(image_folder, filename)
        image = pygame.image.load(image_path)
        image = resize_image(image, (TILE_SIZE, TILE_SIZE))
        images.append(image)
    except pygame.error as e:
        print(f"Không thể tải hình ảnh: {filename}. Đường dẫn: {image_path}. Lỗi: {e}")

# Kiểm tra xem số lượng hình ảnh có đủ để tạo ra lưới không
if len(images) < GRID_WIDTH * GRID_HEIGHT:
    print("Không đủ hình ảnh để tạo ra lưới. Vui lòng thêm nhiều hình ảnh hơn.")
    pygame.quit()
    sys.exit()

random.shuffle(images)  # Xáo trộn hình ảnh

# Thiết lập các ô vuông để vẽ gạch
tiles = []
for row in range(GRID_HEIGHT):
    for col in range(GRID_WIDTH):
        x = col * TILE_SIZE + (WIDTH - GRID_WIDTH * TILE_SIZE) // 2
        y = row * TILE_SIZE + (HEIGHT - GRID_HEIGHT * TILE_SIZE) // 2
        rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
        tiles.append(rect)

first_selection = None
second_selection = None
flipped = [False] * (GRID_WIDTH * GRID_HEIGHT)

# Hàm vẽ gạch
def draw_tiles():
    for i, rect in enumerate(tiles):
        if flipped[i]:
            screen.blit(images[i], rect.topleft)
        else:
            pygame.draw.rect(screen, BLACK, rect)
            pygame.draw.rect(screen, RED, rect, 2)

# Hàm menu chính
import pygame
import random
import os
import sys

# Khởi tạo Pygame
pygame.init()

# Thiết lập màn hình
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Lật Hình")

# Khởi tạo font
font = pygame.font.SysFont(None, 40)

# Màu sắc
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Kích thước lưới và gạch
GRID_WIDTH = 4  # Số ô ngang
GRID_HEIGHT = 3  # Số ô dọc
TILE_SIZE = 150  # Kích thước ô

# Tải âm thanh
pygame.mixer.music.load("b.mp3")
pygame.mixer.music.play(-1)  # Phát nhạc nền

# Hàm thu nhỏ hình ảnh
def resize_image(image, size):
    return pygame.transform.scale(image, size)

# Danh sách hình ảnh - Giả định đã có 5 cặp hình ảnh trong thư mục "images"
images = []
image_folder = "images"
image_filenames = [
    "image1.png", "image1.png", 
    "image2.png", "image2.png", 
    "image3.png", "image3.png", 
    "image4.png", "image4.png", 
    "image5.png", "image5.png",
    "image6.png", "image6.png"
]

# Tải và thu nhỏ hình ảnh
for filename in image_filenames:
    try:
        image_path = os.path.join(image_folder, filename)
        image = pygame.image.load(image_path)
        image = resize_image(image, (TILE_SIZE, TILE_SIZE))
        images.append(image)
    except pygame.error as e:
        print(f"Không thể tải hình ảnh: {filename}. Đường dẫn: {image_path}. Lỗi: {e}")

# Kiểm tra xem số lượng hình ảnh có đủ để tạo ra lưới không
if len(images) < GRID_WIDTH * GRID_HEIGHT:
    print("Không đủ hình ảnh để tạo ra lưới. Vui lòng thêm nhiều hình ảnh hơn.")
    pygame.quit()
    sys.exit()

random.shuffle(images)  # Xáo trộn hình ảnh

# Thiết lập các ô vuông để vẽ gạch
tiles = []
for row in range(GRID_HEIGHT):
    for col in range(GRID_WIDTH):
        x = col * TILE_SIZE + (WIDTH - GRID_WIDTH * TILE_SIZE) // 2
        y = row * TILE_SIZE + (HEIGHT - GRID_HEIGHT * TILE_SIZE) // 2
        rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
        tiles.append(rect)

first_selection = None
second_selection = None
flipped = [False] * (GRID_WIDTH * GRID_HEIGHT)

# Hàm vẽ gạch
def draw_tiles():
    for i, rect in enumerate(tiles):
        if flipped[i]:
            screen.blit(images[i], rect.topleft)
        else:
            pygame.draw.rect(screen, BLACK, rect)
            pygame.draw.rect(screen, RED, rect, 2)

# Hàm menu chính
def main_menu():
    while True:
        screen.fill(WHITE)
        title = font.render("Game Lật Hình", True, RED)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 50))

        start_button = pygame.Rect(WIDTH // 2 - 100, 150, 200, 50)
        register_button = pygame.Rect(WIDTH // 2 - 100, 220, 200, 50)
        login_button = pygame.Rect(WIDTH // 2 - 100, 290, 200, 50)
        exit_button = pygame.Rect(WIDTH // 2 - 100, 360, 200, 50)

        pygame.draw.rect(screen, BLACK, start_button)
        pygame.draw.rect(screen, BLACK, register_button)
        pygame.draw.rect(screen, BLACK, login_button)
        pygame.draw.rect(screen, BLACK, exit_button)

        start_text = font.render("Bắt Đầu", True, WHITE)
        register_text = font.render("Đăng Ký", True, WHITE)
        login_text = font.render("Đăng Nhập", True, WHITE)
        exit_text = font.render("Thoát", True, WHITE)

        screen.blit(start_text, (start_button.x + (start_button.width - start_text.get_width()) // 2, start_button.y + 10))
        screen.blit(register_text, (register_button.x + (register_button.width - register_text.get_width()) // 2, register_button.y + 10))
        screen.blit(login_text, (login_button.x + (login_button.width - login_text.get_width()) // 2, login_button.y + 10))
        screen.blit(exit_text, (exit_button.x + (exit_button.width - exit_text.get_width()) // 2, exit_button.y + 10))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    return "start"
                elif register_button.collidepoint(event.pos):
                    return "register"
                elif login_button.collidepoint(event.pos):
                    return "login"
                elif exit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

# Vòng lặp trò chơi chính
while True:
    choice = main_menu()

    if choice == "start":
        break

# Chạy vòng lặp trò chơi
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for i, rect in enumerate(tiles):
                if rect.collidepoint(pos):
                    if not flipped[i]:
                        if first_selection is None:
                            first_selection = i
                            flipped[first_selection] = True
                        elif second_selection is None and i != first_selection:
                            second_selection = i
                            flipped[second_selection] = True

    screen.fill(WHITE)
    draw_tiles()

    # Kiểm tra xem hai lựa chọn có khớp nhau không
    if first_selection is not None and second_selection is not None:
        if images[first_selection] != images[second_selection]:
            pygame.time.wait(1000)
            flipped[first_selection] = False
            flipped[second_selection] = False
        first_selection = None
        second_selection = None

    pygame.display.flip()

pygame.quit()