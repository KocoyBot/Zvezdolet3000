from pygame.surface import Surface
from Config import Fonts, Colors, Images, Constants
from pygame import mouse
from UI.ButtonUI import ButtonUI
from Game.Player import Player

class GameOverUI:
    def __init__(self, player: Player):
        self.label = Fonts.Zantroke(63).render("Game Over", True, Colors.LIGHT_GRAY)
        self.text_score = Fonts.Zantroke(30).render("Score: " + str(player.score), True, Colors.LIGHT_GRAY)
        self.button_main_menu = ButtonUI(Images.BUTTONS['main_menu']['default'], Images.BUTTONS['main_menu']['hover'], Images.BUTTONS['main_menu']['click'])

    def load(self, display: Surface, mouse_button_down: bool):
        self.mouse_button_down = mouse_button_down
        self.display = display

        self.display.blit(self.label, (self.display.get_width() / 2 - self.label.get_width() / 2, 50))

        self.display.blit(self.text_score, (self.display.get_width() / 2 - self.text_score.get_width() / 2, 300))

        self.button_main_menu.draw(self.display, self.display.get_width() / 2 - self.button_main_menu.get_rect().width / 2, 400)
        self.button_main_menu.is_hover(mouse.get_pos())
        self.button_main_menu.button_mouse_button_down(self.mouse_button_down)
        