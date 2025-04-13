import pygame, random, sys, os

screenWidth = 800
screenHeight = 600
playerSize = 50
playerSpeed = 1
enemySize = 30
enemySpeed = 0.4
enemyCount = 5
bulletSpeed = 2

#Khai báo biến
playerPos = [screenWidth/2, screenHeight-2*playerSize]
enemyList = []
for i in range(enemyCount):
    enemyPos = [random.randint(0, screenWidth-enemySize), random.randint(-100, 0)]
    enemyList.append(enemyPos)

pygame.init()

#Màn hình game
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Game đua xe')

def get_asset_path(filename):
    if hasattr(sys, '_MEIPASS'):
        # Running in a PyInstaller bundle
        return os.path.join(sys._MEIPASS, 'assets', filename)
    else:
        # Running in a development environment
        return os.path.join('assets', filename)
    
car_image = pygame.image.load(get_asset_path('car.png'))
car_image = pygame.transform.scale(car_image, (playerSize, playerSize + 20))
car_image = pygame.transform.flip(car_image, False, True)
redCar = pygame.image.load(get_asset_path('redCar.png'))
redCar = pygame.transform.scale(redCar, (enemySize, enemySize + 20))

# Bullet class
class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 10
        self.color = (255, 0, 0)

    def move(self):
        self.y -= bulletSpeed

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

# List to store bullets
bullets = []

#Hàm vẽ các đối tượng
def DrawObject():
    screen.fill((255,255,255))
    screen.blit(car_image, (playerPos[0], playerPos[1]))
    # pygame.draw.rect(screen, (0,0,0), (playerPos[0], playerPos[1], playerSize, playerSize))
    for enemyPos in enemyList:
        screen.blit(redCar, (enemyPos[0], enemyPos[1]))
        # pygame.draw.rect(screen, (255,0,0), (enemyPos[0], enemyPos[1], enemySize, enemySize))
    for bullet in bullets:
        bullet.draw()

#Hàm cập nhật vị trí của các đối tượng
def UpdateEnemy():
    for idx, enemyPos in enumerate(enemyList):
        if enemyPos[1] >= 0 and enemyPos[1] < screenHeight:
            enemyPos[1] += enemySpeed
        else:
            enemyPos[0] = random.randint(0, screenWidth-enemySize)
            enemyPos[1] = random.randint(-100, 0)

# Hàm cập nhật đạn
def UpdateBullets():
    for bullet in bullets[:]:
        bullet.move()
        if bullet.y < 0:
            bullets.remove(bullet)
        for enemyPos in enemyList[:]:
            if enemyPos[0] < bullet.x < enemyPos[0] + enemySize and enemyPos[1] < bullet.y < enemyPos[1] + enemySize:
                # enemyList.remove(enemyPos)
                enemyPos[0] = random.randint(0, screenWidth-enemySize)
                enemyPos[1] = random.randint(-100, 0)
                bullets.remove(bullet)
                break

#Hàm kiểm tra va chạm giữa 2 đối tượng
def DetectCollision(playerPos, enemyPos):
    p_x = playerPos[0]
    p_y = playerPos[1]
    e_x = enemyPos[0]
    e_y = enemyPos[1]

    if (e_x >= p_x and e_x < (p_x + playerSize)) or (p_x >= e_x and p_x < (e_x + enemySize)):
        if (e_y >= p_y and e_y < (p_y + playerSize)) or (p_y >= e_y and p_y < (e_y + enemySize)):
            return True
    return False

#Hàm trạng thái va chạm
def CollisionStatus():
    for enemyPos in enemyList:
        if DetectCollision(playerPos, enemyPos):
            return True
    return False


#Hàm xử lý sự kiện
def HandleEvents():
    #Sự kiện thoát game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(Bullet(playerPos[0] + playerSize // 2, playerPos[1]))
    #Xử lý sự kiện phím bấm
    keys = pygame.key.get_pressed()     #tuple (); dictionary {}; list []
    if keys[pygame.K_LEFT] and playerPos[0] > 0:
        playerPos[0] -= playerSpeed
    if keys[pygame.K_RIGHT] and playerPos[0] < screenWidth - playerSize:
        playerPos[0] += playerSpeed
    # if keys[pygame.K_UP] and playerPos[1] > 0:
    #     playerPos[1] -= playerSpeed
    # if keys[pygame.K_DOWN] and playerPos[1] < screenHeight - playerSize:
    #     playerPos[1] += playerSpeed
    return False

#Vòng lặp game
score = 0
gameOver = False
while not gameOver:
    #Xử lý sự kiện trong game
    gameOver = HandleEvents()

    #Cập nhật vị trí của kẻ địch
    UpdateEnemy()
    UpdateBullets()
    #Kiểm tra va chạm
    if CollisionStatus():
        gameOver = True
    #Vẽ các đối tượng
    DrawObject()

    score += 1
    if score % 5000 == 0:
        enemySpeed += 0.1

    #Hiển thị điểm số
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score//10}", True, (0,0,0))
    screen.blit(text, (10,10))

    pygame.display.update()
else:
    screen.fill((255,255,255))
    font = pygame.font.Font(None, 72)
    text = font.render(f"Game Over", True, (0,0,0))
    screen.blit(text, (screenWidth//2 - 150, screenHeight//2 - 50))
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score//10}", True, (0,0,0))
    screen.blit(text, (screenWidth//2 - 50, screenHeight//2))
    pygame.display.update()
    pygame.time.wait(3000)