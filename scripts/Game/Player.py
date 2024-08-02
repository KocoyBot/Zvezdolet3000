from pygame.sprite import Sprite
from pygame.surface import Surface
from Config import Constants, Images
import pygame

class Player(Sprite):
    def __init__(self, x: int, y: int, img: Surface, players_lives: int):
        super().__init__()
        self.x = x
        self.y = y
        self.img = img.convert_alpha()
        self.rect = self.img.get_rect()
        self.rect.center = (self.x, self.y)
        self.lives = players_lives
        self.score = 0

    def draw(self, display: Surface):
        self.display = display
        self.display.blit(self.img, self.rect)

    def update(self):
        self.rect.x = pygame.mouse.get_pos()[0] - self.rect.width // 2
        self.rect.y = pygame.mouse.get_pos()[1] - self.rect.height // 2

        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= Constants.WIDTH_WINDOW - self.rect.width:
            self.rect.x = Constants.WIDTH_WINDOW - self.rect.width

        if self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.y >= Constants.HEIGHT_WINDOW - self.rect.height:
            self.rect.y = Constants.HEIGHT_WINDOW - self.rect.height

    def check_lives(self):
        if self.lives <= 0:
            return True
        return False

    