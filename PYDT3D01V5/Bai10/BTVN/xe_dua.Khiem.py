import pygame,datetime,random,sys
from pygame.locals import QUIT
pygame.init()
font=pygame.font.SysFont('Times New Roman',45)
Screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('Dua Xe')
chieu_rong=500
chieu_cao=500
Screen.fill((255,255,255))
Kich_thuoc_nv=20
Kich_thuoc_ke_dich=20
Toc_do_nv=10
Toc_do_ke_dich=20
So_luong_ke_dich=15
player_pos=[int(chieu_rong//2),int(chieu_cao-Kich_thuoc_nv)]
enemy_list=[]
mau_dich=(255,0,0)
mau_nv=(0,0,0)
clock=pygame.time.Clock()
for i in range(So_luong_ke_dich):
    enemy_pos = [random.randint(0,(chieu_rong-20)//2)*2,random.randint(-6,-1)*20]
    enemy_list.append(enemy_pos)
def chay():
    pygame.draw.rect(Screen,mau_nv,[player_pos[0],player_pos[1],Kich_thuoc_nv,Kich_thuoc_nv],0)
    for enemy_pos in enemy_list:
        pygame.draw.rect(Screen,mau_dich,[enemy_pos[0],enemy_pos[1],Kich_thuoc_ke_dich,Kich_thuoc_ke_dich],0)
def update():
     Screen.fill((255,255,255))
     for i in range(len(enemy_list)):
        if enemy_list[i][1]>=0 and enemy_list[i][1]<chieu_cao:
               enemy_list[i][1]+=Toc_do_ke_dich
        else:
             enemy_list[i][0]=random.randint(0,(chieu_rong-20)//2)*2
             enemy_list[i][1]=random.randint(-6,0)*20
game_over=False
def check(obj1_pos, obj2_pos):
    obj1_x = obj1_pos[0]
    obj1_y = obj1_pos[1]
    obj2_x = obj2_pos[0]
    obj2_y = obj2_pos[1]
    if (obj1_x >= obj2_x and obj1_x < (obj2_x + Kich_thuoc_ke_dich)) or (obj2_x >= obj1_x and obj2_x < (obj1_x + Kich_thuoc_nv)):
        if (obj1_y >= obj2_y and obj1_y < (obj2_y + Kich_thuoc_ke_dich)) or (obj2_y >= obj1_y and obj2_y < (obj1_y + Kich_thuoc_nv)):
            return True
    return False
def kiem_tra():
    for enemy_pos in enemy_list:
        if check(player_pos, enemy_pos):
            return True
    return False
screen=False
text_="Hello bấm cách để tiếp tục"
text=font.render(text_,True,(0,255,0))
textRect=text.get_rect()
textRect.center=(255,255)
Screen.blit(text,textRect)
diem=0
mang=3
while not game_over:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                screen=not screen
    if screen ==True:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == QUIT:
                game_over=True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_pos[0] > 0:
            player_pos=[player_pos[0]-Toc_do_nv,player_pos[1]]
        if keys[pygame.K_RIGHT] and player_pos[0] < chieu_cao -Kich_thuoc_nv:
            player_pos=[player_pos[0]+Toc_do_nv,player_pos[1]]
        update()
        chay()
        diem+=1
        a="Score: " + str(diem) 
        text=font.render(a,True,(0,0,0))
        Screen.blit(text,(0,0))
        b="Mang: " + str(mang) 
        text=font.render(b,True,(0,0,0))
        Screen.blit(text,(300,0))
        if kiem_tra()==True and mang>0:
            mang-=1
        if mang ==0:
            print(diem)
            game_over=True
        if diem%500==0:
            mang+=3
    pygame.display.update()