import pygame
import math
pygame.init()

class oiseau:
    def __init__(self, x, y):
        self.health = 10
        self.image = pygame.image.load("images/personnages/chicken.png")
        self.image = pygame.transform.scale(self.image, (87, 90))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.click = False

    @staticmethod
    def cheminoiseau(startx, starty, power, ang, time):
        velx = math.cos(ang) * power + 50
        vely = math.sin(ang) * power / 2

        distx = velx * time
        # équation de trajectoire ici
        # distY = (vely * time) + ((-4.9 * (time)**2) /2)
        gravite = 10
        hauteur = 10
        disty = -1 / 2 * gravite * (distx / velx) ** 2 + power * vely * (distx / velx) + hauteur

        newx = round(distx + startx)
        newy = round(starty - disty)

        return newx, newy


class loup:
    def __init__(self):
        self.health = 10
        self.image = pygame.image.load("images/personnages/Wolf.png")
        self.image = pygame.transform.scale(self.image, (90, 75))
        self.rect = self.image.get_bounding_rect()
        self.rect.x = 1350
        self.rect.y = 603
        self.touche = 0


class loup2:
    def __init__(self):
        self.health = 10
        self.image = pygame.image.load("images/personnages/Wolf.png")
        self.image = pygame.transform.scale(self.image, (90, 75))
        self.rect = self.image.get_bounding_rect()
        self.rect.x = 1150
        self.rect.y = 817
        self.touche = 0


class bloc_bois:
    def __init__(self):
        self.health = 10
        self.image = pygame.image.load("images/blocs/bloc bois.png")
        self.rect = self.image.get_rect()


class grosse_boule:
    def __init__(self):
        self.health = 10
        self.image = pygame.image.load("images/blocs/boule grosse bois.png")
        self.rect = self.image.get_rect()
        self.x = 1200
        self.y = 250


class petite_boule:
    def __init__(self):
        self.health = 10
        self.image = pygame.image.load("images/blocs/boule petite bois.png")
        self.rect = self.image.get_rect()
        self.x = 1200
        self.y = 500


class petit_bout_bois:
    def __init__(self):
        self.image = pygame.image.load("images/blocs/petit bout de bois.png")
        self.image = pygame.transform.scale(self.image, (21, 200))
        self.rect = self.image.get_rect()
        self.rect.x = 1500
        self.rect.y = 685
        self.touche = 0


class petit_bout_bois2:
    def __init__(self):
        self.image = pygame.image.load("images/blocs/petit bout de bois.png")
        self.image = pygame.transform.scale(self.image, (21, 200))
        self.rect = self.image.get_rect()
        self.rect.x = 1300
        self.rect.y = 685
        self.touche = 0


class petit_bout_bois3:
    def __init__(self):
        self.image = pygame.image.load("images/blocs/petit bout de bois.png")
        self.image = pygame.transform.scale(self.image, (21, 200))
        self.rect = self.image.get_rect()
        self.rect.x = 1300
        self.rect.y = 500
        self.touche = 0


class petit_bout_bois4:
    def __init__(self):
        self.image = pygame.image.load("images/blocs/petit bout de bois.png")
        self.image = pygame.transform.scale(self.image, (21, 200))
        self.rect = self.image.get_rect()
        self.rect.x = 1500
        self.rect.y = 500
        self.touche = 0


class petit_bout_bois5:
    def __init__(self):
        self.image = pygame.image.load("images/blocs/petit bout de bois.png")
        self.image = pygame.transform.scale(self.image, (21, 200))
        self.rect = self.image.get_rect()
        self.rect.x = 1100
        self.rect.y = 685
        self.touche = 0


class rectangle_bois:
    def __init__(self):
        self.health = 10
        self.image = pygame.image.load("images/blocs/image bout de bois.png")
        self.image = pygame.transform.scale(self.image, (200, 21))
        self.rect = self.image.get_rect()
        self.rect.x = 1310
        self.rect.y = 670
        self.touche = 0


class rectangle_bois2:
    def __init__(self):
        self.health = 10
        self.image = pygame.image.load("images/blocs/image bout de bois.png")
        self.image = pygame.transform.scale(self.image, (200, 21))
        self.rect = self.image.get_rect()
        self.rect.x = 1310
        self.rect.y = 500
        self.touche = 0


class rectangle_bois3:
    def __init__(self):
        self.health = 10
        self.image = pygame.image.load("images/blocs/image bout de bois.png")
        self.image = pygame.transform.scale(self.image, (200, 21))
        self.rect = self.image.get_rect()
        self.rect.x = 1110
        self.rect.y = 670
        self.touche = 0


class triangle_bois:
    def __init__(self):
        self.health = 10
        self.image = pygame.image.load("images/blocs/triangle bois.png")
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = self.image.get_rect()
        self.rect.x = 908
        self.rect.y = 682
        self.touche = 0
