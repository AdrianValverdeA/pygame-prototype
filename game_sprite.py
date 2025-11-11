import pygame

class GameSprite(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

    def clone(self):
        raise NotImplementedError("clone() ha d'estar implementat")
