from pygame.surface import Surface
from pygame import SRCALPHA

class Cropping:
    def __init__(self, img: Surface, x_start: int, y_start: int, x_stop: int, y_stop: int):
        self.img = img

        self.x_start = x_start
        self.y_start = y_start
        self.x_stop = x_stop
        self.y_stop = y_stop

        self.cropped_surface = Surface((self.x_stop-self.x_start, self.y_stop-self.y_start), SRCALPHA, 32)

    def crop(self):
        self.cropped_surface.blit(self.img, (0, 0), (self.x_start, self.y_start, self.x_stop-self.x_start, self.y_stop-self.y_start))
        return self.cropped_surface
