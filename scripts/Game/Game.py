import pygame
from Config import Constants, Images, Sounds, Fonts
from Game.Player import Player
from Game.Background import Background
from Game.Pulya import Pulya
from random import randint
from Game.Planets import Planets
from Game.Meteorite import Meteorite

class Game:
    def __init__(self) -> None:
        self.player = Player(100, 100, Images.ZVEZDOLET, Constants.PLAYERS_LIVES)
        self.background = Background(Images.BACKGROUND)
        self.pulki = pygame.sprite.Group()
        self.planets = pygame.sprite.Group()
        self.meteorites = pygame.sprite.Group()

    def create_pulya(self):
        return Pulya(self.player.rect.x+50, self.player.rect.y+35, Images.PULYA, Constants.SPEED_PULYA, self.pulki)
                
    
    def create_planet(self):
        size = randint(50, 150)
        img = pygame.transform.scale(Images.PLANETS[1], (size, size))
        x = randint(0, Constants.WIDTH_WINDOW-img.get_rect().width)
        y = randint(-Constants.HEIGHT_WINDOW, -img.get_rect().height)
        return Planets(x, y, img, self.planets)
    
    def create_meteorite(self):
        size = 75
        angle = randint(0, 360)
        img = pygame.transform.scale(Images.METEORITE, (size, size))
        img = pygame.transform.rotate(img, angle)
        x = randint(img.get_rect().width, Constants.WIDTH_WINDOW-img.get_rect().width)
        y = randint(-Constants.HEIGHT_WINDOW, -img.get_rect().height)
        return Meteorite(x, y, img, Constants.SPEED_METEORITES, self.meteorites, self.player)
    
    def collide_pulki_to_meteorites(self):
        if pygame.sprite.groupcollide(self.pulki, self.meteorites, True, True):
            self.player.score += 1

    def load(self, display: pygame.surface.Surface, set_sound: bool):
        self.display = display
        self.set_sound = set_sound
        self.score_text = Fonts.Zantroke(25).render("Score: " + str(self.player.score), True, (255, 255, 255))
        self.lives_text = Fonts.Zantroke(25).render("Lives: " + str(self.player.lives), True, (255, 255, 255))
        self.background.draw(self.display)
        self.background.update()
        self.planets.draw(self.display)
        self.planets.update()
        self.meteorites.draw(self.display)
        self.meteorites.update()
        self.pulki.draw(self.display)
        self.pulki.update()
        self.player.draw(self.display)
        self.player.update()
        self.collide_pulki_to_meteorites()
        self.display.blit(self.score_text, (10, 10))
        self.display.blit(self.lives_text, (10, 40))