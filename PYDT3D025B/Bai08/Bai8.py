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
blue = (0, 0, 255)
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
board = [[0 for i in range(boardCols)] for j in range(boardRows)]           #comprehension
# board = [[1,0,0],
#          [0,2,2],
#          [1,2,0]]  # Khởi tạo board rỗng
# #comprehension

# Vẽ các line
def drawLines():
    #Horizontal lines
    pygame.draw.line(screen, lineColor, (0, squareSize), (width, squareSize), lineWidth)
    pygame.draw.line(screen, lineColor, (0, 2 * squareSize), (width, 2 * squareSize), lineWidth)
    #Vertical lines
    pygame.draw.line(screen, lineColor, (squareSize, 0), (squareSize, height), lineWidth)
    pygame.draw.line(screen, lineColor, (2 * squareSize, 0), (2 * squareSize, height), lineWidth)

#Xác định ô được chọn thuộc người chơi nào
def markSquare(row, col, player):       #player = 1(X) hoặc 2 (O)
    board[row][col] = player

#Vẽ X-O
#(Red, greeen, blue) = (0, 0, 255)
def drawFigures():
    for row in range(boardRows):
        for col in range(boardCols):
            if board[row][col] == 1:
                pygame.draw.line(screen, crossColor, (col * squareSize + space, row * squareSize + squareSize - space), (col * squareSize + squareSize - space, row * squareSize + space), crossWidth)
                pygame.draw.line(screen, crossColor, (col * squareSize + space, row * squareSize + space), (col * squareSize + squareSize - space, row * squareSize + squareSize - space), crossWidth)
            elif board[row][col] == 2:
                pygame.draw.circle(screen, circleColor, (int(col * squareSize + squareSize // 2), int(row * squareSize + squareSize // 2)), circleRadius, circleWidth)

#Kiểm tra ô trống
def availableSquare(row, col):
    return board[row][col] == 0

#Kiểm tra người chơi thắng
def checkWin(player):
    # Kiểm tra hàng ngang
    for row in range(boardRows):
        if (board[row][0] == player and board[row][1] == player and board[row][2] == player):
            drawHorizontalWinningLine(row)
            return True
    # Kiểm tra hàng dọc
    for col in range(boardCols):
        if (board[0][col] == player and board[1][col] == player and board[2][col] == player):
            drawVerticalWinningLine(col)
            return True
    # Kiểm tra đường chéo
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        drawAscDiagonalWinningLine()
        return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        drawDescDiagonalWinningLine()
        return True
    return False            #người chơi hiện tại chưa chiến thắng

# Vẽ đường ngang
def drawHorizontalWinningLine(row):
    posY = row * squareSize + squareSize // 2
    pygame.draw.line(screen, red, (15, posY), (width - 15, posY), 15)
# Vẽ đường dọc
def drawVerticalWinningLine(col):
    posX = col * squareSize + squareSize // 2
    pygame.draw.line(screen, red, (posX, 15), (posX, height - 15), 15)
# Vẽ đường chéo
def drawAscDiagonalWinningLine():
    pygame.draw.line(screen, red, (15, height - 15), (width - 15, 15), 15)
# Vẽ đường chéo
def drawDescDiagonalWinningLine():
    pygame.draw.line(screen, red, (15, 15), (width - 15, height - 15), 15)

font = pygame.font.SysFont('Arial', 24, True, True)
def showWinner(player):
    if player == 1:
        text = font.render('X Win!', True, blue)
    else:
        text = font.render('O Win!', True, blue)
    textRect = text.get_rect(center=(width // 2, height // 2))
    screen.blit(text, textRect)

def restart():
    screen.fill(bgColor)
    drawLines()
    global board, gameOver, player
    player = 1
    gameOver = False
    for row in range(boardRows):
        for col in range(boardCols):
            board[row][col] = 0

drawLines()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not gameOver:
            mouseX = event.pos[0]   # x chuột       event.pos = (x, y)
            mouseY = event.pos[1]   # y chuột
            
            clickedRow = int(mouseY // squareSize)
            clickedCol = int(mouseX // squareSize)

            if availableSquare(clickedRow, clickedCol):
                markSquare(clickedRow, clickedCol, player)
                drawFigures()
                if checkWin(player):
                    gameOver = True
                    showWinner(player)
                player = player % 2 + 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
        pygame.display.update()