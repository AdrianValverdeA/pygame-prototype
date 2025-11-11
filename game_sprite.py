import pygame

class GameSprite(pygame.sprite.Sprite):
    def clone(self):
        raise NotImplementedError("clone() must be implemented")
