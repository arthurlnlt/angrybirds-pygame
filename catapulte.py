import pygame

pygame.init()


class catapulte(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/personnages/catapulte.png")
        self.image = pygame.transform.scale(self.image, (500, 300))
        self.rect = self.image.get_rect()
        self.rect.x = -100
        self.rect.y = 625
