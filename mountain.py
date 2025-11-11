import pygame
import random
from pygame.locals import RLEACCEL

from screen import Screen
from game_sprite import GameSprite

# Define the Mountain object extending pygame.sprite.Sprite
# Use an image for a better looking sprite
class Mountain(GameSprite):
    def __init__(self):
        super(Mountain, self).__init__()
        self.surf = pygame.image.load("icons/mountain.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # The starting position is randomly generated
        self.rect = self.surf.get_rect(
            center = ( Screen.width, Screen.height)
        )

    # Move the cloud based on a constant speed
    # Remove it when it passes the left edge of the screen.py
    def update(self):
        speedx = -5
        speedy = -1
        if self.rect.top < Screen.height - 99:
            speedy = 0
        self.rect.move_ip(speedx, speedy)
        if self.rect.right < 0:
            self.kill()

    def clone(self):
        return Mountain()