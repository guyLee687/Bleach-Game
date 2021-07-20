import pygame 
from pygame import mixer
from menos_grande import menosGrande

'''
This file is simply just to test the movement and behaviour of 
characters in game. 
'''

pygame.init() 

win = pygame.display.set_mode((1280, 720))

# Background
background = pygame.image.load('background_img/test_background.png')

# Caption and Icon
pygame.display.set_caption("NovaCore Bleach Game")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# Sound
mixer.music.load("backgroundMusic.wav")
mixer.music.play(-1)

# Game clock frame/sec
clock = pygame.time.Clock()
menos_list = []

menos_Count = 0
win.blit(background, (0, 0))
pygame.display.update()  
pygame.time.delay(5000) 
while True: 
    clock.tick(27)
    win.fill((0,0,0))
    win.blit(background, (0, 0))

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit()

    if menos_Count % 50 == 0 and len(menos_list) < 10:
        menos_list.append(menosGrande.MenosGrande(100, 450, 64, 64))
    menos_Count += 1

    for men in menos_list: 
        men.pace(win, 100, 1100) 
    
    pygame.display.update()  

