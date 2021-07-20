import pygame
from pygame import mixer

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((1280, 720))

# Background
background = pygame.image.load('background.png')

# Sound
mixer.music.load("backgroundMusic.wav")
mixer.music.play(-1)

# Caption and Icon
pygame.display.set_caption("NovaCore Bleach Game")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# Buttons
# white color
color = (255, 255, 255)

# light shade of the button
color_light = (170, 170, 170)

# dark shade of the button
color_dark = (100, 100, 100)

# stores the width of the
# screen into a variable
width = screen.get_width()

# stores the height of the
# screen into a variable
height = screen.get_height()

# defining a font
smallfont = pygame.font.SysFont('Corbel', 35)

# rendering a text written in
# this font
startButton = smallfont.render('Start', True, color)
quitButton = smallfont.render('Quit', True, color)

while True:

    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()

        # checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:

            # if the mouse is clicked on the
            # button the game is terminated
            if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2.5 <= mouse[1] <= height / 2.5 + 40:
                pygame.image.load(background)
            elif width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                pygame.quit()

        # Background Image
        screen.blit(background, (0, 0))

    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()

    # if mouse is hovered on a button it
    # changes to lighter shade
    if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2.5 <= mouse[1] <= height / 2.5 + 40:
        pygame.draw.rect(screen, color_light, [width / 2, height / 2.5, 140, 40])

    elif width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
        pygame.draw.rect(screen, color_light, [width / 2, height / 2, 140, 40])

    else:
        pygame.draw.rect(screen, color_dark, [width / 2, height / 2.5, 140, 40])
        pygame.draw.rect(screen, color_dark, [width / 2, height / 2, 140, 40])

    # superimposing the text onto our button
    screen.blit(startButton, (width / 2 + 50, height / 2.5))
    screen.blit(quitButton, (width / 2 + 50, height / 2))
    pygame.display.update()