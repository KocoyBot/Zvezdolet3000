from pygame.sprite import Sprite
from pygame.surface import Surface
import pygame

class Pulya(Sprite):
    def __init__(self, x: int, y: int, img: Surface, speed: int, group: pygame.sprite.Group):
        super().__init__()
        self.image = img.convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.add(group)

    def update(self):
        self.rect.y -= self.speed

        if self.rect.y < 0-self.rect.height:
            self.kill()