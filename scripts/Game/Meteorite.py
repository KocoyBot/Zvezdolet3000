from pygame.sprite import Sprite
from pygame.surface import Surface
import pygame
from Config import Constants
from Game.Player import Player
from Game.Pulya import Pulya

class Meteorite(Sprite):
    def __init__(self, x: int, y: int, img: Surface, speed: int, group: pygame.sprite.Group, player: Player):
        super().__init__()
        self.image = img.convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.player = player
        self.add(group)

    def update(self):
        self.rect.y += self.speed

        if self.rect.y >= Constants.HEIGHT_WINDOW + self.rect.height:
            self.kill()
            self.player.lives -= 1
        
        if self.rect.colliderect(self.player.rect):
            self.kill()
            self.player.lives -= 1

            