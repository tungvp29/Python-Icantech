import pygame, sys 

pygame.init()

width = 300  
height = 300 
line_width = 7 
board_rows = 3
board_cols = 3
square_size = 100
circle_radius = 30
circle_width = 7
cross_width = 12
space = 27 

RED = (255, 0, 0)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic Tac Toe")

font = pygame.font.Font(None, 40)

board = [[0 for i in range(board_cols)] for j in range(board_rows)]

def draw_lines():
    pygame.draw.line(screen, LINE_COLOR, (0, square_size), (width, square_size), line_width)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * square_size), (width, 2 * square_size), line_width)
    pygame.draw.line(screen, LINE_COLOR, (square_size, 0), (square_size, height), line_width)
    pygame.draw.line(screen, LINE_COLOR, (2 * square_size, 0), (2 * square_size, height), line_width)

def draw_figures():
    for row in range(board_rows):
        for col in range(board_cols):
            if board[row][col] == 1:
                pygame.draw.line(screen, CROSS_COLOR, (col * square_size + space, row * square_size + space), 
                                 (col * square_size + square_size - space, row * square_size + square_size - space), cross_width)
                pygame.draw.line(screen, CROSS_COLOR, (col * square_size + space, row * square_size + square_size - space), 
                                 (col * square_size + square_size - space, row * square_size + space), cross_width)
            elif board[row][col] == 2:
                pygame.draw.circle(screen, CIRCLE_COLOR, 
                                   (int(col * square_size + square_size // 2), int(row * square_size + square_size // 2)), 
                                   circle_radius, circle_width)

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] == 0

def is_board_full():
    for row in range(board_rows):
        for col in range(board_cols):
            if board[row][col] == 0:
                return False
    return True

def draw_vertical_winning_line(col, color):
    posX = col * square_size + square_size // 2
    pygame.draw.line(screen, color, (posX, 15), (posX, height - 15), 15)

def draw_horizontal_winning_line(row, color):
    posY = row * square_size + square_size // 2
    pygame.draw.line(screen, color, (15, posY), (width - 15, posY), 15)

def draw_asc_diagonal(color):
    pygame.draw.line(screen, color, (15, height - 15), (width - 15, 15), 15)

def draw_desc_diagonal(color):
    pygame.draw.line(screen, color, (15, 15), (width - 15, height - 15), 15)

def check_win(player):
    color = CIRCLE_COLOR if player == 2 else CROSS_COLOR
    for col in range(board_cols):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, color)
            return True
    for row in range(board_rows):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row, color)
            return True
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(color)
        return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(color)
        return True
    return False

def display_winner(winner):
    text = font.render(f" {winner} Win!", True, RED)
    screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))
    pygame.display.update()

def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    for row in range(board_rows):
        for col in range(board_cols):
            board[row][col] = 0

screen.fill(BG_COLOR)
draw_lines()

player = 1
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            clicked_row = int(mouseY // square_size)
            clicked_col = int(mouseX // square_size)
            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player)
                draw_figures()
                if check_win(player):
                    game_over = True
                    winner = "O" if player == 2 else "X"
                    display_winner(winner)
                elif is_board_full():
                    game_over = True
                    text = font.render("Trò chơi hòa!", True, RED)
                    screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))
                    pygame.display.update()
                player = player % 2 + 1 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                game_over = False
        pygame.display.update()
