import pygame, sys, random
from pygame.locals import QUIT
pygame.init()  
WIDTH = 300
HEIGHT = 300
LINE_WIDTH = 7
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = 100
CIRCLE_RADIUS = 30
CIRCLE_WIDTH = 7
CROSS_WIDTH = 12
SPACE = 27
# RGB colors
RED = (255, 0, 0)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill(BG_COLOR)
board = []
Black = (0,0,0)
for i in range(BOARD_ROWS):
    board.append([])
    for j in range(BOARD_COLS):
        board[i].append(0)
player = 1
def draw_table():
    pygame.draw.line(screen, Black, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE),2)
    pygame.draw.line(screen, Black, (0, SQUARE_SIZE*2), (WIDTH, SQUARE_SIZE*2),2)
    pygame.draw.line(screen, Black, (SQUARE_SIZE,0), (SQUARE_SIZE,HEIGHT),2)
    pygame.draw.line(screen, Black, (SQUARE_SIZE*2,0), (SQUARE_SIZE*2,HEIGHT),2)
def check_available(row,col):
    return board[row][col] == 0
def mark(row,col,player):
    board[row][col]=player
CROSS_COLOR= (255,0,0)
CIRCLE_COLOR = (0,255,0)
SPACE = 27
def draw(col, row):
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), 4)
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), 4)
            elif board[row][col] == 2:
                pygame.draw.circle(screen, CIRCLE_COLOR, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2 - SPACE, 4)
def check_win(player):
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col)
            return True
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row)
            return True
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal()
        return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal()
        return True
    return False
def draw_vertical_winning_line(col):
    posX = col * SQUARE_SIZE + SQUARE_SIZE // 2
    color = RED
    pygame.draw.line(screen, color, (posX, 15), (posX, HEIGHT - 15), 15)
def draw_horizontal_winning_line(row):
    posY = row * SQUARE_SIZE + SQUARE_SIZE // 2
    color = RED
    pygame.draw.line(screen, color, (15, posY), (WIDTH - 15, posY), 15)
def draw_asc_diagonal():
    color = RED
    pygame.draw.line(screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), 15)
def draw_desc_diagonal():
    color = RED
    pygame.draw.line(screen, color, (15, 15),(WIDTH - 15, HEIGHT - 15), 15)
def restart():
    screen.fill(BG_COLOR)
    draw_table()
    player = 1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0
draw_table()
player = 1
game_over = False
def draw_figures():
    for row in range (BOARD_ROWS):
        for col in range (BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.line (screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line (screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)
            elif board [row] [col] == 2:
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
def mark_square (row, col, player):
    board [row][col] = player
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        if event.type == pygame. MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos [0]
            mouseY = event.pos [1]
            clicked_row = int(mouseY // SQUARE_SIZE)
            clicked_col = int(mouseX // SQUARE_SIZE)
            if check_available(clicked_row, clicked_col):
                mark_square (clicked_row, clicked_col, player)
                if check_win(player):
                    game_over = True
                player=player % 2 + 1
                draw_figures()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                game_over = False
    pygame.display.update()