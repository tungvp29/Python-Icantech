import pygame, random

pygame.init()

#Match game
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
font = pygame.font.Font(None, 48)

pygame.mixer.Sound.load("sound.wav")