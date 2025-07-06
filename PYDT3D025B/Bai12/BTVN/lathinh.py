import pygame, random
pygame.init()
width = 680
height = 488
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Game Lật Hình')
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK =(0,0,0)
font = pygame.font.SysFont(None,48)
images = []
for i in range(1,9):
    image =pygame.image.load(f"img{i}.png")
    images.append(image)
    images.append(image)
random.shuffle(images)
tilesize = 64
gridwidth = 4
gridheight = 4
padding = 20
gridx = (width - gridwidth * (tilesize + padding) + padding)//2
gridy = (height - gridheight * (tilesize + padding) + padding)//2
tiles = []
for row in range(gridheight):
    for col in range(gridwidth):
        image = images.pop()
        x = gridx + col * (tilesize + padding)
        y = gridy + row * (tilesize + padding)
        tile = (x,y,tilesize,tilesize, image, False)
        tiles.append(tile)
score = 0
fliptiles = []
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for i, tile in enumerate(tiles):
                if tile[0] < pos[0] < tile[0] + tilesize and \
                    tile[1] < pos[1] < tile[1] + tilesize and \
                        not tile[5]:
                            tile = tile[:5] + (True, )
                            tiles[i] = tile
                            fliptiles.append(i)
                            if len(fliptiles) == 2:
                                if tiles[fliptiles[0]][4] == tiles[fliptiles[1]][4]:
                                    score += 1
                                    fliptiles = []
                                else:
                                    pygame.time.wait(1000)
                                    for i in fliptiles:
                                        tile = tiles[i][:5] + (False, )
                                        tiles[i] = tile
                                    fliptiles =[]
    screen.fill(WHITE)
    for tile in tiles:
        pygame.draw.rect(screen, BLACK, tile[:4])
        if tile[5]:
            screen.blit(tile[4], tile[:2])
    scoretext = font.render(f"Score: {score}", True, BLACK)
    screen.blit(scoretext, (20,20))
    pygame.display.flip()
    win = False
    if score == 8:
        win = True
    if win:
        text = font.render('WINNER!', True, RED)
        textrect = text.get_rect(center=(width//2, height//2))
        screen.blit(text, textrect)
        pygame.display.flip()
pygame.quit()        