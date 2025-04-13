import pygame, sys

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
blue = (50, 153, 213)
red = (213, 50, 80)
green = (0, 255, 0)

screen = pygame.display.set_mode((1000, 700))
screen.fill(white)

#Khiêm
pygame.draw.rect(screen,black,[50,50,100,50], 2)
pygame.draw.ellipse(screen,black,[50,50,100,50])

#Hưng
pygame.draw.rect(screen,red,[300,200,100,50], 2)
pygame.draw.ellipse(screen,red,[300,200,100,50])

#Bảo An
pygame.draw.rect(screen,blue,[450,350,250,150], 2)
pygame.draw.ellipse(screen,blue,[450,350,250,150])

#Huy
# pygame.draw.ellipse()

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        try:
            if event.type == pygame.KEYDOWN:
                print('Key pressed')
                if event.key == pygame.K_LEFT:
                    print('Left key pressed')
        except:
            print('Key pressed')
            diem=0
            while True:
                print("NO may.NO may.NO may.NO may.NO may.NO may.NO may.NO may.NO may.NO may.NO may.NO may.")
                diem+=1
                a=open("{diem}.txt",'a')
    pygame.display.update()