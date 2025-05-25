import pygame, sys
from pygame.locals import QUIT

pygame.init()

#Thông số cấu hình
width, height = 300, 300
lineWidth = 7
boardRows, boardCols = 3, 3
squareSize = 100        #141, 46        1, 0
circleRadius = 30
circleWidth = 7
crossWidth = 12
space = 27
red = (255, 0, 0)
bgColor = (28, 170, 156)
lineColor = (23, 145, 135)
circleColor = (239, 231, 200)
crossColor = (66, 66, 66)
player = 1
gameOver = False

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(bgColor)

# Board
# board = [[0 for i in range(boardCols)] for j in range(boardRows)]           #comprehension
board = [[0,0,0],
         [0,0,0],
         [0,0,0]]  # Khởi tạo board rỗng
# board = []
# for i in range(boardRows):
#     for j in range(boardCols):
#         board[i][j] = 0
# #comprehension

# Vẽ các line
def drawLines():
    #Horizontal lines
    pygame.draw.line(screen, lineColor, (0, squareSize), (width, squareSize), lineWidth)
    pygame.draw.line(screen, lineColor, (0, 2 * squareSize), (width, 2 * squareSize), lineWidth)
    #Vertical lines
    pygame.draw.line(screen, lineColor, (squareSize, 0), (squareSize, height), lineWidth)
    pygame.draw.line(screen, lineColor, (2 * squareSize, 0), (2 * squareSize, height), lineWidth)

clock = pygame.time.Clock()

while True:
    clock.tick(30)  # Giới hạn FPS
    pygame.display.update()
