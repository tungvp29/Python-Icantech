import pygame, random 

SCREEN_WIDTH = 800 
SCREEN_HEIGHT = 600  
PLAYER_SIZE = 50  
PLAYER_SPEED = 1 
ENEMY_SIZE = 30  
ENEMY_SPEED = 0.2  
ENEMY_COUNT = 5  
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)


vtnc = [SCREEN_WIDTH/2, SCREEN_HEIGHT-PLAYER_SIZE] 
vtkd = []  
for i in range(ENEMY_COUNT):
    enemy_pos = [random.randint(0, SCREEN_WIDTH - ENEMY_SIZE), random.randint(-100, 0)] 
    vtkd.append(enemy_pos)  


pygame.init()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game đua xe") 
def ve():
    screen.fill(WHITE)
    pygame.draw.rect(screen,BLUE,(vtnc[0],vtnc[1],PLAYER_SIZE,PLAYER_SIZE))
    for u in vtkd:
        pygame.draw.rect(screen,RED,(u[0],u[1],ENEMY_SIZE,ENEMY_SIZE))
def cnkd():
    for i in range(len(vtkd)):
        if vtkd[i][1]>=0 and vtkd[i][1]<SCREEN_HEIGHT:
            vtkd[i][1]+=ENEMY_SPEED
        else:
            vtkd[i][0]=random.randint(0,SCREEN_WIDTH-ENEMY_SIZE)
            vtkd[i][1]=random.randint(-100,0)
def xlsk():
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            return True
gameover=False
while not gameover:
    gameover=xlsk()
    cnkd()
    ve()
    pygame.display.update()
    

    
    