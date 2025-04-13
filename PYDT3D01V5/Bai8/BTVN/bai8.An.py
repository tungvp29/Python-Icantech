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
SPACE = 27
font=pygame.font.Font(None,20)
MAUFONT=(255,255,255)


RED = (255, 0, 0)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BG_COLOR)

board = [[0 for i in range(BOARD_COLS)] for j in range(BOARD_ROWS)]

def draw_lines():
    
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    
   
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), CIRCLE_RADIUS, CIRCLE_WIDTH)

def mark_square(row, col, player):
    board[row][col] = player
def available_square(row, col):
    if board[row][col] == 0:
        return True
def ve_dthang(col):
    posx = col * SQUARE_SIZE + SQUARE_SIZE // 2
    MAU=RED
    pygame.draw.line(screen,MAU,(posx,15),(posx,HEIGHT-15),15)
def ve_dngang(row):
    posy=row*SQUARE_SIZE+SQUARE_SIZE//2
    MAU=RED
    pygame.draw.line(screen,MAU,(15,posy),(WIDTH-15,posy),15)
def ve_dcheotraiphai():
    MAU=RED
    pygame.draw.line(screen,RED,(15,HEIGHT-15),(WIDTH-15,15),15)
def ve_dcheophaitrai():
    MAU=RED
    pygame.draw.line(screen,RED,(15,15),(WIDTH-15,HEIGHT-15),15)
def checkwin(player):
    for col in range(BOARD_COLS):
        if board[0][col]==board[1][col]==board[2][col]==player:
            ve_dthang(col)
            return True
    for row in range(BOARD_ROWS):
        if board[row][0]==board[row][1]==board[row][2]==player:
            ve_dngang(row)
            return True
    if board[2][0]==board[1][1]==board[0][2]==player:
        ve_dcheotraiphai()
        return True
    if board[0][0]==board[1][1]==board[2][2]==player:
        ve_dcheophaitrai()
        return True
    return False
def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    player=1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col]=0
def ve_tbct(player):
    if player==1:
        text=font.render("PLAYER 1 IS THE WINNER",True,MAUFONT)
    else:
         text=font.render("PLAYER 2 IS THE WINNER",True,MAUFONT)
    text_rect=text.get_rect(center=(WIDTH//2,HEIGHT//2))
    screen.blit(text,text_rect)
player = 1
game_over = False
draw_lines()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if  event.type==pygame.MOUSEBUTTONDOWN and not game_over:
            chuotx=event.pos[0]
            chuoty=event.pos[1]
            nhan_row=int(chuoty//SQUARE_SIZE)
            nhan_col=int(chuotx//SQUARE_SIZE)
            if available_square(nhan_row,nhan_col):
                mark_square(nhan_row,nhan_col,player)
                draw_figures()
                if checkwin(player):
                    game_over=True
                    ve_tbct(player)
                player=player%2+1
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_r:
                restart()
                game_over=False
        pygame.display.update()
                
                    
        
    


    





