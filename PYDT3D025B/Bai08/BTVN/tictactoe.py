import pygame, sys
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
SPACE= 27
RED = (255,0,0)
BG_COLOR = (28,170,156)
LINE_COLOR = (23,145,135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66,66,66)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BG_COLOR)

board = [[0 for i in range(BOARD_COLS)] for j in range(BOARD_ROWS)]
def draw_lines():
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2*SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2*SQUARE_SIZE, HEIGHT), LINE_WIDTH)
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.line(screen,CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE),CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE//2), int(row * SQUARE_SIZE + SQUARE_SIZE //2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
def mark_square(row,col,player):
    board[row][col]= player
def available_square(row,col):
    if board[row][col] == 0:
        return True
def check_win(player):
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col)
            return True
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] ==player:
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
    pygame.draw.line(screen, RED, (posX,15), (posX, HEIGHT - 15), 15)
def draw_horizontal_winning_line(row):
    posY = row * SQUARE_SIZE + SQUARE_SIZE // 2
    pygame.draw.line(screen, RED, (15, posY), (WIDTH - 15, posY), 15)
def draw_asc_diagonal():
    pygame.draw.line(screen, RED, (15, HEIGHT - 15), (WIDTH - 15, 15), 15)
def draw_desc_diagonal():
    pygame.draw.line(screen, RED, (15, 15), (WIDTH - 15, HEIGHT - 15), 15)
def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    player = 1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0
font = pygame.font.SysFont('Arial', 24, True, True)
def showWinner(player):
    if player == 1:
        text = font.render('X Win!', True, (255,255,255))
    else:
        text=font.render('O Win!', True, (255,255,255))
    textRect = text.get_rect(center= (WIDTH//2, HEIGHT //2))
    screen.blit(text, textRect)    
    
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
            clicked_row = int(mouseY // SQUARE_SIZE)
            clicked_col = int(mouseX // SQUARE_SIZE)
            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player)
                if check_win(player):
                    game_over = True
                    showWinner(player)
                player = player % 2 + 1
                draw_figures()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                game_over = False

        pygame.display.update()
            