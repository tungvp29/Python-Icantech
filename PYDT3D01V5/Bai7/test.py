import pygame, sys, random
from pygame.locals import QUIT
pygame.init()
width = 300
height = 300
screen = pygame.display.set_mode((width,height))
screen.fill((255, 255, 255))  
pygame.display.flip()
table = []
square_size = 100
board_row = 3
board_col = 3
Black = (0, 0, 0)

for i in range(board_row):
    table.append([])
    for j in range(board_col):
        table[i].append(0)
player = 1
def draw_table():
    pygame.draw.line(screen, Black, (0, square_size), (width, square_size),2)
    pygame.draw.line(screen, Black, (0, square_size*2), (width, square_size*2),2)
    pygame.draw.line(screen, Black, (square_size,0), (square_size,height),2)
    pygame.draw.line(screen, Black, (square_size*2,0), (square_size*2,height),2)
def check_available(row,col):
    #return table[row][col] == 0
    if table[row][col] == 0:
        return True
    return False
def mark(row,col,player):
    table[row][col]=player
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos  
            table_col = mouse_x // square_size  
            table_row = mouse_y // square_size  
            if check_available(table_row,table_col):
                mark(table_row,table_col,player)
                print(table)
    draw_table()
    pygame.display.update()
