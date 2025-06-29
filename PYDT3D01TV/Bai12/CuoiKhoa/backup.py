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

# # Tải âm thanh
# pygame.mixer.music.load("a.mp3")
# pygame.mixer.music.play(-1)  # Phát nhạc nền

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