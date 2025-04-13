import sys

import pygame
from pygame.locals import QUIT

pygame.init()
height = 450
width = 450
line_width = 5
board_rows = 3
board_columns = 3
square_size = 150
circle_radius = 50
circle_width = 15
cross_width = 25
space = 25
red = (255, 0, 0)
bg_color = (28, 170, 156)
black = (0, 0, 0)
line_color = (0, 0, 0)
circle_color = (255, 255, 255)
cross_color = (255, 255, 255)
dis = pygame.display.set_mode((height, width))
pygame.display.set_caption('Tick tac toe!')
dis.fill(black)
board = [[0 for i in range(board_columns)]for j in range(board_rows)]
def draw_lines():
    pygame.draw.line(dis, line_color, (0, square_size), (width, square_size), line_width)
    pygame.draw.line(dis, line_color, (0, 2 * square_size), (width, 2 * square_size), line_width)
    pygame.draw.line(dis, line_color, (square_size, 0), (square_size, height), line_width)
    pygame.draw.line(dis, line_color, (2 * square_size, 0), (2 * square_size, height), line_width)
    pygame.draw.line(dis, cross_color, (175, 15), (175, 435), 15)
def draw_figures():
    for row in range(board_rows):
        for col in range(board_columns):
            if board[row][col] == 1:
                #pygame.draw.line(dis, cross_color, (col * square_size + space, row * square_size - space), (col * square_size + square_size - space, row * square_size + square_size + space), cross_width)
                pygame.draw.line(dis, cross_color, (col * square_size + space, row * square_size + space), (col * square_size + square_size - space, row * square_size + square_size - space), cross_width)
            elif board[row][col] == 2:
                pygame.draw.circle(dis, circle_color,(int(col * square_size + square_size // 2),int(row * square_size + square_size // 2)), circle_radius, circle_width)
def mark_square(row, column, player):
    board[row][column] = player
def available_square(row, column):
    if board[row][column] == 0:
        return True
    return False

def draw_vertical_winning_line(col, player):
    posX = col * square_size + square_size // 2
    print('posX ', posX)
    # pygame.draw.line(dis, red, (posX, 15), (posX, height - 15), 15)
    pygame.draw.line(dis, cross_color, (175, 15), (175, 435), 15)
    print('draw finished')
    pygame.display.update()
def draw_horizontal_winning_line(row, player):
    posY = row * square_size + square_size // 2
    pygame.draw.line(dis, red, (15, posY), (width - 15, posY), 15)
def draw_asc_diagonal(player):
    color = red
    pygame.draw.line(dis, color, (15, height - 15), (width - 15, 15), 15)
def draw_desc_diagonal(player):
    color = red
    pygame.draw.line(dis, color, (15, 15), (width - 15, height - 15), 15)
def check_win(player):
    print(board)
    for col in range(board_columns):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True
    for row in range(board_rows):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True
    return False

def restart():
    dis.fill(bg_color)
    draw_lines()
    player = 1
    for row in range(board_rows):
        for col in range(board_columns):
            board[row][col]  = 0
draw_lines()
player = 1
game_over = False
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mousex = event.pos[0]
            mousey = event.pos[1]
            clicked_row = int(mousey // square_size)
            clicked_col = int(mousex // square_size)
            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player)
                if check_win(player):
                    game_over = True

                player = 2 if player == 1 else 1
    dis.fill(bg_color)
    draw_lines()
    draw_figures()
    pygame.display.update()