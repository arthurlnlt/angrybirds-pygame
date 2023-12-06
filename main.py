import time as tme

import pygame

from menu import *
from jeu import *
from classes import *

pygame.init()

# initialisation des classes
oiseau = oiseau(110, 650)
jeu = jeu()

# initialisation de la trajectoire
x = 0
y = 0
time = 0
power = 0
angle = 0
shoot = False

# initialisation de la fenêtre de jeu
pygame.display.set_caption("Angry birds")
screen = pygame.display.set_mode((1600, 1000))
background = pygame.image.load("images/fonds/fondjeu.jpg")
background = pygame.transform.scale(background, (1900, 1000))
fond_fin_partie = pygame.image.load("images/fonds/game-over.png")
musique = pygame.mixer.music.load("musique/Angry Birds Theme Song.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)
coupdepoing = pygame.mixer.Sound("musique/coupdepoing.mp3")

# initialisation des boucles / conditions d'arrêt
partie_terminee = False
partie_gagnee = False
running = True
moving = False

# initialisation des compteurs de touche des loups et oiseaux
compteurtouche = 1
compteur_loup_touche = 0
compteur_oiseau = 0

# initialisation du score
font = pygame.font.Font('freesansbold.ttf', 32)
count = 0
count3 = 0
count2 = 0
TextX = 100
TextY = 100
etoile1 = pygame.image.load("images/blocs/etoile.png")
etoile2 = pygame.image.load("images/blocs/etoile.png")
etoile3 = pygame.image.load("images/blocs/etoile.png")


def show_score(x, y):
    score = font.render("Score : " + str(count3), True, (0, 0, 0))
    screen.blit(score, (x, y))


while running:
    show_score(TextX, TextY)
    pygame.display.update()
    if shoot is True:
        show_score(TextX, TextY)
        if oiseau.rect.y <= 810:
            time += 0.1
            po = oiseau.cheminoiseau(x, y, power, angle, time)
            oiseau.rect.x = po[0]
            oiseau.rect.y = po[1]
            if jeu.loup.touche == 1 and compteur_loup_touche != 69:
                if partie_gagnee is False:
                    coupdepoing.play()
                shoot = False
                oiseau.rect.x = 110
                oiseau.rect.y = 650
                compteur_loup_touche = 69
                # score
                if count == 0:
                    count += 100
                    count -= (compteur_oiseau * 20)
                    count3 = count + count2

            if jeu.loup2.touche == 1 and compteur_loup_touche != 79:
                if partie_gagnee is False:
                    coupdepoing.play()
                shoot = False
                oiseau.rect.x = 110
                oiseau.rect.y = 650
                compteur_loup_touche = 79
                # score
                if count2 == 0:
                    count2 += 100
                    count2 -= (compteur_oiseau * 20)
                    count3 = count + count2

        else:
            shoot = False
            tme.sleep(0.5)
            # l'oiseau revient à sa position de départ
            oiseau.rect.x = 110
            oiseau.rect.y = 650
            compteur_oiseau += 1
            # ici pour arrêter au bout de n essais
            if compteur_oiseau == 5:
                partie_terminee = True

    # détection de la touche des objets par l'oiseau
    if oiseau.rect.colliderect(jeu.loup.rect):
        jeu.loup.touche = 1
    if oiseau.rect.colliderect(jeu.loup2.rect):
        jeu.loup2.touche = 1
    if oiseau.rect.colliderect(jeu.petit_bout_bois.rect):
        jeu.petit_bout_bois.touche = 1
    if oiseau.rect.colliderect(jeu.petit_bout_bois2.rect):
        jeu.petit_bout_bois2.touche = 1
    if oiseau.rect.colliderect(jeu.rectangle_bois.rect):
        jeu.rectangle_bois.touche = 1
    if oiseau.rect.colliderect(jeu.petit_bout_bois3.rect):
        jeu.petit_bout_bois3.touche = 1
    if oiseau.rect.colliderect(jeu.petit_bout_bois4.rect):
        jeu.petit_bout_bois4.touche = 1
    if oiseau.rect.colliderect(jeu.petit_bout_bois5.rect):
        jeu.petit_bout_bois5.touche = 1
    if oiseau.rect.colliderect(jeu.rectangle_bois2.rect):
        jeu.rectangle_bois2.touche = 1
    if oiseau.rect.colliderect(jeu.rectangle_bois3.rect):
        jeu.rectangle_bois3.touche = 1
    if oiseau.rect.colliderect(jeu.triangle_bois.rect):
        jeu.triangle_bois.touche = 1

    if partie_terminee is False:
        # affichage des différents composants du niveau
        screen.blit(background, (0, 0))
        show_score(TextX, TextY)
        screen.blit(jeu.catapulte.image, jeu.catapulte.rect)
        screen.blit(oiseau.image, (oiseau.rect.x, oiseau.rect.y))
        # affichage des objets selon s'ils ont étés touchés par l'oiseau ou non
        if jeu.petit_bout_bois3.touche == 0:
            screen.blit(jeu.petit_bout_bois3.image, (jeu.petit_bout_bois3.rect.x, jeu.petit_bout_bois3.rect.y))
        if jeu.petit_bout_bois2.touche == 0:
            screen.blit(jeu.petit_bout_bois2.image, (jeu.petit_bout_bois2.rect.x, jeu.petit_bout_bois2.rect.y))
        if jeu.petit_bout_bois4.touche == 0:
            screen.blit(jeu.petit_bout_bois4.image, (jeu.petit_bout_bois4.rect.x, jeu.petit_bout_bois4.rect.y))
        if jeu.petit_bout_bois5.touche == 0:
            screen.blit(jeu.petit_bout_bois5.image, (jeu.petit_bout_bois5.rect.x, jeu.petit_bout_bois5.rect.y))
        if jeu.loup.touche == 0:
            screen.blit(jeu.loup.image, (jeu.loup.rect.x, jeu.loup.rect.y))
        if jeu.loup2.touche == 0:
            screen.blit(jeu.loup2.image, (jeu.loup2.rect.x, jeu.loup2.rect.y))
        if jeu.petit_bout_bois.touche == 0:
            screen.blit(jeu.petit_bout_bois.image, (jeu.petit_bout_bois.rect.x, jeu.petit_bout_bois.rect.y))
        if jeu.rectangle_bois.touche == 0:
            screen.blit(jeu.rectangle_bois.image, (jeu.rectangle_bois.rect.x, jeu.rectangle_bois.rect.y))
        if jeu.rectangle_bois2.touche == 0:
            screen.blit(jeu.rectangle_bois2.image, (jeu.rectangle_bois2.rect.x, jeu.rectangle_bois2.rect.y))
        if jeu.rectangle_bois3.touche == 0:
            screen.blit(jeu.rectangle_bois3.image, (jeu.rectangle_bois3.rect.x, jeu.rectangle_bois3.rect.y))
        if jeu.triangle_bois.touche == 0:
            screen.blit(jeu.triangle_bois.image, (jeu.triangle_bois.rect.x, jeu.triangle_bois.rect.y))

    pos = pygame.mouse.get_pos()
    # ajustement à la taille de l'oiseau
    line = [(oiseau.rect.x + 43, oiseau.rect.y + 45), pos]

    if jeu.loup.touche == 1 and jeu.loup2.touche == 1:
        partie_gagnee = True
        # affichage des étoiles à la fin du niveau
        if count3 == 200:
            screen.blit(etoile1, (450, 400))
            screen.blit(etoile2, (673, 400))
            screen.blit(etoile3, (896, 400))

        if 200 > count3 >= 100:
            screen.blit(etoile1, (450, 400))
            screen.blit(etoile2, (673, 400))
        if count3 <= 100 and count3 != 0:
            screen.blit(etoile1, (450, 400))
        pygame.display.update()

    # affichage du game over si le nombre d'essais est dépassé
    if compteur_oiseau == 5 and partie_terminee is True:
        screen.blit(fond_fin_partie, (450, 400))
        pygame.display.update()

    pygame.display.update()

    # Acquisition des évènements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pause(screen)
        if event.type == pygame.MOUSEBUTTONUP:
            oiseau.click = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if shoot is False:
                shoot = True
                x = oiseau.rect.x
                y = oiseau.rect.y
                time = 0
                power = math.sqrt((line[1][1] - line[0][1]) ** 2 + (line[1][0] - line[0][0]) ** 2) / 50
                angle = findangle(pos, oiseau)
            position = pygame.mouse.get_pos()

