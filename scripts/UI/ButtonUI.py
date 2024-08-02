from pygame.surface import Surface
from Config import Sounds
from pygame import Rect

class ButtonUI:
    def __init__(self, img: Surface, img_on_hover: Surface, img_on_mouse_down: Surface):
        self.img = img
        self.default_img = self.img
        self.img_on_hover = img_on_hover
        self.img_on_mouse_down = img_on_mouse_down
        self.isHover = False

    def get_rect(self) -> Rect:
        return self.img.get_rect()

    def draw(self, display: Surface, x: int, y: int):
        self.display = display
        self.x = x
        self.y = y
        self.rect = self.display.blit(self.img, (self.x, self.y))
    
    def is_hover(self, mouse_pos):
        self.isHover = self.rect.collidepoint(mouse_pos)
        if self.isHover:
            self.img = self.img_on_hover
        else:
            self.img = self.default_img
            
    def button_mouse_button_down(self, mouse_button_down: bool):
        if mouse_button_down and self.isHover:
            self.img = self.img_on_mouse_down

    def button_mouse_button_up(self):
        if self.isHover:
            return True
        return False