import pygame,datetime,random,sys
from pygame.locals import QUIT
pygame.init()
font=pygame.font.SysFont('Times New Roman',45)
do_dai=[]
diem=0
chieu_dai=1
an=0
do_dai_con_ran=10
toa_do_x=240
toa_do_y=240
thay_doi_x=0
thay_doi_y=0
nen=(0,0,0)
Color_Food_and_Snake=(255,255,255)
pygame.init()
Screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('Ran san moi')
Screen.fill((0,0,0))
clock=pygame.time.Clock()
text=font.render("Hello bấm cách để tiếp tục",True,(0,255,0))
textRect=text.get_rect()
textRect.center=(255,255)
screen=0
Screen.blit(text,textRect)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                screen=1
        pygame.display.update()
    if screen==1:
            if an==0:
                an_x=random.randint(1,49)*10
                an_y=random.randint(1,49)*10
                an=1
            clock.tick(12+diem)
            for event in pygame.event.get():
                if event.type == QUIT:
                    Screen.fill(nen)
                    text=font.render("Bye",True,(0,255,0))
                    textRect=text.get_rect()
                    textRect.center=(255,255)
                    Screen.blit(text,textRect)
                    time.sleep(2)
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and thay_doi_y!=10 :
                   thay_doi_y=-10
                   thay_doi_x=0
                if event.key == pygame.K_DOWN and thay_doi_y!=-10:
                    thay_doi_y=10
                    thay_doi_x=0
                if event.key == pygame.K_LEFT and thay_doi_x!=10:
                    thay_doi_x=-10
                    thay_doi_y=0
                if event.key == pygame.K_RIGHT and thay_doi_x!=-10:
                    thay_doi_x=10
                    thay_doi_y=0
            toa_do_x+=thay_doi_x
            toa_do_y+=thay_doi_y
            do_dai.append([toa_do_x,toa_do_y])
            if len(do_dai)>chieu_dai:
                del do_dai[0]
            Screen.fill(nen)
            pygame.draw.rect(Screen,Color_Food_and_Snake,[toa_do_x,toa_do_y,do_dai_con_ran,do_dai_con_ran],0)
            pygame.draw.rect(Screen,Color_Food_and_Snake,[an_x,an_y,do_dai_con_ran,do_dai_con_ran],0)
            for i in range(chieu_dai):
                pygame.draw.rect(Screen,Color_Food_and_Snake,[do_dai[i][0],do_dai[i][1],do_dai_con_ran,do_dai_con_ran],0)
            for i in range(chieu_dai):
                if i!=chieu_dai-1:
                    if toa_do_x == do_dai[i][0]and toa_do_y== do_dai[i][1]:
                            Screen.fill(nen)
                            text=font.render("Lai",True,(0,255,0))
                            textRect=text.get_rect()
                            textRect.center=(255,255)
                            Screen.blit(text,textRect)
                            pygame.display.update()
                            do_dai=[]
                            diem=0
                            chieu_dai=1
                            an=0
                            do_dai_con_ran=10
                            toa_do_x=240
                            toa_do_y=240
                            thay_doi_x=0
                            thay_doi_y=0
            if toa_do_x==an_x and toa_do_y==an_y:
                an=0
                diem+=1
                chieu_dai+=1
            if toa_do_x<0:
                 toa_do_x = 490
            elif toa_do_x>490:
                 toa_do_x=0
            elif toa_do_y<0:
                 toa_do_y=490
            elif toa_do_y>490:
                 toa_do_y=0
            a="Score: " + str(diem)
            text=font.render(a,True,(255,255,255))
            Screen.blit(text,(0,0))
            pygame.display.update()