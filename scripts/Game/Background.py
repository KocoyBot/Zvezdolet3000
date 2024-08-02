from pygame.surface import Surface
from pygame.transform import flip
from Config import Constants

class Background:
    def __init__(self, img: Surface):
        self.img = img
        self.y1 = 0
        self.y2 = -Constants.HEIGHT_WINDOW

    def draw(self, display: Surface):
        display.blit(self.img, (0, self.y1))

        display.blit(flip(self.img, False, True), (0, self.y2))

    def update(self):
        self.y1 += 5
        self.y2 += 5
        
        if self.y1 >= Constants.HEIGHT_WINDOW:
            self.y1 = - Constants.HEIGHT_WINDOW

        if self.y2 >= Constants.HEIGHT_WINDOW:
            self.y2 = - Constants.HEIGHT_WINDOW
            

    