from pygame.surface import Surface
from Config import Fonts, Colors, Images, Constants
from pygame import mouse
from UI.ButtonUI import ButtonUI

class MainMenuUI:
    def __init__(self):
        self.lable = Fonts.Zantroke(63).render("Zvezdolet3000", True, Colors.LIGHT_GRAY)
        self.version = Fonts.Zantroke(20).render(Constants.VERSION, True, Colors.LIGHT_GRAY)
        self.button_play = ButtonUI(Images.BUTTONS['play']['default'], Images.BUTTONS['play']['hover'], Images.BUTTONS['play']['click'])
        self.button_options = ButtonUI(Images.BUTTONS['options']['default'], Images.BUTTONS['options']['hover'], Images.BUTTONS['options']['click'])
        self.button_credits = ButtonUI(Images.BUTTONS['credits']['default'], Images.BUTTONS['credits']['hover'], Images.BUTTONS['credits']['click'])
        self.button_exit = ButtonUI(Images.BUTTONS['exit']['default'], Images.BUTTONS['exit']['hover'], Images.BUTTONS['exit']['click'])

    def load(self, display: Surface, mouse_button_down: bool):
        self.mouse_button_down = mouse_button_down
        self.display = display

        self.display.blit(self.lable, (self.display.get_width() / 2 - self.lable.get_width() / 2, 50))

        self.display.blit(Images.ZVEZDOLET_FOR_MAIN_MENU, (480, 150))

        self.display.blit(self.version, (self.display.get_width() - self.version.get_width() - 5, self.display.get_height() - self.version.get_height() - 5))

        self.button_play.draw(self.display, self.display.get_width() / 2 - 250, 200)
        self.button_play.is_hover(mouse.get_pos())
        self.button_play.button_mouse_button_down(self.mouse_button_down)

        self.button_options.draw(self.display, self.display.get_width() / 2 - 260, 300)
        self.button_options.is_hover(mouse.get_pos())
        self.button_options.button_mouse_button_down(self.mouse_button_down)

        self.button_credits.draw(self.display, self.display.get_width() / 2 - 270, 405)
        self.button_credits.is_hover(mouse.get_pos())
        self.button_credits.button_mouse_button_down(self.mouse_button_down)

        self.button_exit.draw(self.display, self.display.get_width() / 2 - 250, 505)
        self.button_exit.is_hover(mouse.get_pos())
        self.button_exit.button_mouse_button_down(self.mouse_button_down)
        