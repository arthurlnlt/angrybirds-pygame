import math
import pygame
import button

pygame.init()

# trouve l'angle entre l'oiseau et la souris
def findangle(pos, objet):
    sX = objet.rect.x
    sY = objet.rect.y
    try:
        angle = math.atan((sY - pos[1]) / (sX - pos[0]))
    except:
        angle = math.pi / 2

    # Part que sur les x positifs --> x négatif ne part pas
    if pos[1] < sY and pos[0] > sX:
        angle = abs(angle)
    elif pos[1] < sY and pos[0] < sX:
        angle = math.pi - angle
    elif pos[1] > sY and pos[0] < sX:
        angle = math.pi - abs(angle)
    elif pos[1] > sY and pos[0] > sX:
        angle = (math.pi * 2) + angle

    return angle

# menu pause
def pause(screen):
    # check if the options menu is open

    paused = True
    while paused:
        # cadre_img = pygame.image.load("images/fonds/cadre.png").convert_alpha()
        resume_img = pygame.image.load("images/fonds/button_resume.png").convert_alpha()
        quit_img = pygame.image.load("images/fonds/button_quit.png").convert_alpha()

        resume_button = button.bouton(640, 300, resume_img, 1)
        quit_button = button.bouton(670, 400, quit_img, 1)
        menu_state = "options"

        if menu_state == "options":
            if quit_button.draw(screen):
                quit()

            if resume_button.draw(screen):
                paused = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        pygame.display.update()
