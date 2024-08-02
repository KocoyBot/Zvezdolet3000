from pygame.surface import Surface
from pygame.sprite import Sprite
import pygame
from Config import Constants, Images

class Planets(Sprite):
    def __init__(self, x: int, y: int, img: Surface, group: pygame.sprite.Group):
        super().__init__()
        self.image = img.convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.add(group)

    def update(self):
        self.rect.y += 2.5

        if self.rect.y >= Constants.HEIGHT_WINDOW:
            self.kill()