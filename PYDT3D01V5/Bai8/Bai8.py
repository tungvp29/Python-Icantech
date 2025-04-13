import pygame, sys
from pygame.locals import QUIT

pygame.init()

#Thông số cấu hình
width, height = 300, 300
lineWidth = 7
boardRows, boardCols = 3, 3
squareSize = 100
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
board = [[0 for i in range(boardCols)] for j in range(boardRows)]

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

#Vẽ line chiến thắng dọc
def drawVerticalWinningLine(col):
    posX = col * squareSize + squareSize // 2
    color = red
    pygame.draw.line(screen, color, (posX, 15), (posX, height - 15), 15)

#Vẽ line chiến thắng ngang
def drawHorizontalWinningLine(row):
    posY = row * squareSize + squareSize // 2
    color = red
    pygame.draw.line(screen, color, (15, posY), (width - 15, posY), 15)

#Vẽ line chiến thắng chéo
def drawAscendingDiagonal():
    color = red
    pygame.draw.line(screen, color, (15, height - 15), (width - 15, 15), 15)

#Vẽ line chiến thắng chéo
def drawDescendingDiagonal():
    color = red
    pygame.draw.line(screen, color, (15, 15), (width - 15, height - 15), 15)

#Thông báo chiến thắng
def winMessage(player):
    font = pygame.font.Font(None, 24)
    text = font.render('Player ' + str(player) + ' wins!', True, (0,0,0))
    rect = text.get_rect()
    rect.center = (width // 2, height // 2)
    padding = 10
    background_rect = pygame.Rect(
        rect.left - padding,
        rect.top - padding,
        rect.width + 2 * padding,
        rect.height + 2 * padding
    )
    pygame.draw.rect(screen, (255,255,255), background_rect)
    screen.blit(text, rect)

def checkWin(player):
    #vertical win check
    for col in range(boardCols):
        if board[0][col] == board[1][col] == board[2][col] == player:
            drawVerticalWinningLine(col)
            return True
    #horizontal win check
    for row in range(boardRows):
        if board[row][0] == board[row][1] == board[row][2] == player:
            drawHorizontalWinningLine(row)
            return True
    #ascending diagonal win check
    if board[2][0] == board[1][1] == board[0][2] == player:
        drawAscendingDiagonal()
        return True
    #descending diagonal win check
    if board[0][0] == board[1][1] == board[2][2] == player:
        drawDescendingDiagonal()
        return True
    return False

#Khởi tạo lại game
def restart():
    screen.fill(bgColor)
    drawLines()
    player = 1
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
            mouseX = event.pos[0]   # x chuột
            mouseY = event.pos[1]   # y chuột
            
            clickedRow = int(mouseY // squareSize)
            clickedCol = int(mouseX // squareSize)

            if availableSquare(clickedRow, clickedCol):
                markSquare(clickedRow, clickedCol, player)
                if checkWin(player):
                    gameOver = True
                player = player % 2 + 1
                drawFigures()
        pygame.display.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                gameOver = False
        if gameOver:
            winMessage(player)
        pygame.display.update()