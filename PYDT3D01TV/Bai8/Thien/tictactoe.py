import pygame, sys

pygame.init()

line_width = 10
square_size = 100
board_size = 3
cross_color = (6, 43, 69)
circle_color = (227, 213, 163)
win_line_color = (255, 0, 0)
txt_color = (0, 0, 0)
popup_color = (34, 107, 102)
player = 1

screen_size = board_size * square_size
DISPLAYSURF = pygame.display.set_mode((screen_size, screen_size))
DISPLAYSURF.fill((19, 196, 172))

space = 25

font = pygame.font.Font(None, 36)
pygame.display.set_caption("Tic Tac Toe")
clock = pygame.time.Clock()

# Drawing the grid lines
for i in range(board_size - 1):
    pygame.draw.line(DISPLAYSURF, (13, 130, 114), (screen_size / board_size * (i + 1), 0), (screen_size / board_size * (i + 1), screen_size), line_width)
    pygame.draw.line(DISPLAYSURF, (13, 130, 114), (0, screen_size / 3 * (i + 1)), (screen_size, screen_size / 3 * (i + 1)), line_width)

board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

def draw():
    DISPLAYSURF.fill((19, 196, 172))
    # Redrawing the grid lines
    for i in range(board_size - 1):
        pygame.draw.line(DISPLAYSURF, (13, 130, 114), (screen_size / board_size * (i + 1), 0), (screen_size / board_size * (i + 1), screen_size), line_width)
        pygame.draw.line(DISPLAYSURF, (13, 130, 114), (0, screen_size / 3 * (i + 1)), (screen_size, screen_size / 3 * (i + 1)), line_width)
    
    for row in range(board_size):
        for col in range(board_size):
            if board[row][col] == 1:
                pygame.draw.line(DISPLAYSURF, cross_color, (col * square_size + space, row * square_size + space), 
                                 (col * square_size + square_size - space, row * square_size + square_size - space), line_width)
                pygame.draw.line(DISPLAYSURF, cross_color, (col * square_size + square_size - space, row * square_size + space), 
                                 (col * square_size + space, row * square_size + square_size - space), line_width)
            elif board[row][col] == 2:
                pygame.draw.circle(DISPLAYSURF, circle_color, 
                                   (col * square_size + square_size // 2, row * square_size + square_size // 2), 
                                   square_size // 2 - space, line_width)

def mark(row, column, player):
    board[row][column] = player

def available(row, column):
    return board[row][column] == 0

def check_win(player):
    for row in range(board_size):
        if board[row][0] == board[row][1] == board[row][2] == player:
            return ("row", row)
    
    for col in range(board_size):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return ("col", col)
    
    if board[0][0] == board[1][1] == board[2][2] == player:
        return ("diag", 1)
    if board[0][2] == board[1][1] == board[2][0] == player:
        return ("diag", 2)
    return None

def is_board_full():
    for row in board:
        if 0 in row:
            return False
    return True

def draw_win_line(win_type, index):
    if win_type == "row":
        start_pos = (space, index * square_size + square_size // 2)
        end_pos = (screen_size - space, index * square_size + square_size // 2)
    elif win_type == "col":
        start_pos = (index * square_size + square_size // 2, space)
        end_pos = (index * square_size + square_size // 2, screen_size - space)
    elif win_type == "diag":
        if index == 1:
            start_pos = (space, space)
            end_pos = (screen_size - space, screen_size - space)
        elif index == 2:
            start_pos = (screen_size - space, space)
            end_pos = (space, screen_size - space)
    
    pygame.draw.line(DISPLAYSURF, win_line_color, start_pos, end_pos, line_width)

def restart():
    global board, player
    board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    player = 1
    draw()

def restart_screen():
    DISPLAYSURF.fill((19, 196, 172))
    
    play_again_text = font.render("Play Again", True, (0, 0, 0))
    quit_text = font.render("Quit", True, (0, 0, 0))
    
    play_again_rect = play_again_text.get_rect(center=(screen_size // 2, screen_size // 2 - 50))
    quit_rect = quit_text.get_rect(center=(screen_size // 2, screen_size // 2 + 50))
    
    DISPLAYSURF.blit(play_again_text, play_again_rect)
    DISPLAYSURF.blit(quit_text, quit_rect)
    
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if play_again_rect.collidepoint(pos):
                    restart()
                    return
                if quit_rect.collidepoint(pos):
                    pygame.quit()
                    sys.exit()

def handle_winner_or_draw(winner):
    if winner:
        win_type, index = winner
        draw_win_line(win_type, index)
        win_player = font.render(f'Player {player} wins!', True, txt_color)
    else:
        win_player = font.render('Draw!', True, txt_color)

    back_rect = win_player.get_rect(center=(screen_size // 2, screen_size // 2))
    pygame.draw.rect(DISPLAYSURF, popup_color, (back_rect[0] - 10, back_rect[1] - 10, back_rect[2] + 20, back_rect[3] + 20))
    DISPLAYSURF.blit(win_player, back_rect)
    pygame.display.update()

    pygame.time.wait(1500)  # Pause to show the result for 1.5 seconds
    restart_screen()  # Show the restart screen after the result

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            clicked_row = pos[1] // square_size
            clicked_column = pos[0] // square_size
            if available(clicked_row, clicked_column):
                mark(clicked_row, clicked_column, player)
                draw()
                win_result = check_win(player)
                if win_result:
                    handle_winner_or_draw(win_result)
                elif is_board_full():
                    handle_winner_or_draw(None)
                else:
                    player = player % 2 + 1
    pygame.display.update()
