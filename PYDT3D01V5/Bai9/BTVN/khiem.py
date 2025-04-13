import pygame,datetime,random,sys
from pygame.locals import QUIT
pygame.init()
Screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('Dua Xe')
chieu_rong=500
chieu_cao=500
Screen.fill((255,255,255))
Kich_thuoc_nv=20
Kich_thuoc_ke_dich=20
Toc_do_nv=1
Toc_do_ke_dich=3
So_luong_ke_dich=10
player_pos=[chieu_rong/2,chieu_cao-Kich_thuoc_nv]
enemy_list=[]
mau_dich=(255,0,0)
mau_nv=(0,0,0)
for i in range(So_luong_ke_dich):
    enemy_pos = [random.randint(0,chieu_rong-20),random.randint(-100,0)]
    enemy_list.append(enemy_pos)
def chay():
    Screen.fill((255,255,255))
    pygame.draw.rect(Screen,mau_nv,[player_pos[0],player_pos[1],Kich_thuoc_nv,Kich_thuoc_nv],0)
    for enemy_pos in enemy_list:
        pygame.draw.rect(Screen,mau_dich,[enemy_pos[0],enemy_pos[1],Kich_thuoc_ke_dich,Kich_thuoc_ke_dich],0)
def update():
     for i in range(len(enemy_list)):
        if enemy_list[i][1]>=0 and enemy_list[i][1]<chieu_cao:
               enemy_list[i][1]+=Toc_do_ke_dich
        else:
             enemy_list[i][0]=random.randint(0,chieu_rong-Kich_thuoc_ke_dich)
             enemy_list[i][1]=random.randint(-100,0)
game_over=False
while not game_over:
    for event in pygame.event.get():
        if event.type == QUIT:
            game_over=True
    update()
    chay()
    pygame.display.update()