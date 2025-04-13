Do_rong=300
Do_cao=300
import pygame,datetime,random,sys
from pygame.locals import QUIT
pygame.init()
Screen = pygame.display.set_mode((Do_rong,Do_cao))
pygame.display.set_caption('XO')
Screen.fill((255,255,255))
square =100
player=1
space=10
mau_cot=(0,0,0)
chieu_cao_bang=3
chieu_rong_bang=3
toa_do_x=0
toa_do_y=0
bang=[[0 for i in range(chieu_rong_bang)] for i in range(chieu_cao_bang)]
Blue_O=(28, 170, 156)
Red_X=(255,0,0)
#ve duong ke
def cot():
    # Cot
    pygame.draw.rect(Screen,mau_cot,[square-space//2,0,space,Do_cao],0)
    pygame.draw.rect(Screen,mau_cot,[square*2-space//2,0,space,Do_cao],0)
    # Hang
    pygame.draw.rect(Screen,mau_cot,[0,square-space//2,Do_rong,space],0)
    pygame.draw.rect(Screen,mau_cot,[0,square*2-space//2,Do_rong,space],0)
# Kiem tra o da danh hay chua
def check_square(toa_do_x,toa_do_y):
    return bang[toa_do_x][toa_do_y]    
def draw_XO(player,toa_do_x,toa_do_y): 
     if player==1:
           pygame.draw.circle(Screen,Blue_O,(square*(toa_do_x+0.5),square*(toa_do_y+0.5)),20)
cot()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            toa_do_x=event.pos[0]//square
            toa_do_y=event.pos[1]//square
            
            if check_square(toa_do_x,toa_do_y) == 0:
                bang[toa_do_x][toa_do_y] =player
                draw_XO(player,toa_do_x,toa_do_y)
    pygame.display.update()