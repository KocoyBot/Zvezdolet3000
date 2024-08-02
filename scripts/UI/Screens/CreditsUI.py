from pygame.surface import Surface
from Config import Fonts, Colors, Images, Constants
from pygame import mouse
from UI.ButtonUI import ButtonUI

class CreditsUI:
    def __init__(self):
        self.label = Fonts.Zantroke(63).render("Credits", True, Colors.LIGHT_GRAY)
        self.version = Fonts.Zantroke(20).render(Constants.VERSION, True, Colors.LIGHT_GRAY)
        self.text1 = Fonts.Zantroke(20).render(Constants.GAME_NAME + " made by " + Constants.GAME_AUTHOR, True, Colors.LIGHT_GRAY)
        self.text2 = Fonts.Zantroke(20).render("Music and sounds from " + Constants.MUSIC_AND_SOUNDS_PLATFORM, True, Colors.LIGHT_GRAY)
        self.text3 = Fonts.Zantroke(20).render("Textures by " + Constants.GAME_AUTHOR, True, Colors.LIGHT_GRAY)
        self.text4 = Fonts.Zantroke(20).render("The font was taken from the game 'Orion Game'", True, Colors.LIGHT_GRAY)
        self.text5 = Fonts.Zantroke(20).render("Special thanks to " + Constants.SPECIAL_THANKS, True, Colors.LIGHT_GRAY)
        self.text6 = Fonts.Zantroke(20).render("Programming Language: Python", True, Colors.LIGHT_GRAY)
        self.text7 = Fonts.Zantroke(20).render("Framework: PyGame", True, Colors.LIGHT_GRAY)
        self.button_back = ButtonUI(Images.BUTTONS['back']['default'], Images.BUTTONS['back']['hover'], Images.BUTTONS['back']['click'])

    def load(self, display: Surface, mouse_button_down: bool):
        self.mouse_button_down = mouse_button_down
        self.display = display

        self.display.blit(self.label, (self.display.get_width() / 2 - self.label.get_width() / 2, 50))

        self.display.blit(self.version, (self.display.get_width() - self.version.get_width() - 5, self.display.get_height() - self.version.get_height() - 5))

        self.display.blit(self.text1, (self.display.get_width() / 2 - self.text1.get_width() / 2, 200))
        self.display.blit(self.text2, (self.display.get_width() / 2 - self.text2.get_width() / 2, 250))
        self.display.blit(self.text3, (self.display.get_width() / 2 - self.text3.get_width() / 2, 300))
        self.display.blit(self.text4, (self.display.get_width() / 2 - self.text4.get_width() / 2, 350))
        self.display.blit(self.text5, (self.display.get_width() / 2 - self.text5.get_width() / 2, 400))
        self.display.blit(self.text6, (self.display.get_width() / 2 - self.text6.get_width() / 2, 450))
        self.display.blit(self.text7, (self.display.get_width() / 2 - self.text7.get_width() / 2, 500))

        self.button_back.draw(self.display, self.display.get_width() / 2 - 400, 600)
        self.button_back.is_hover(mouse.get_pos())
        self.button_back.button_mouse_button_down(self.mouse_button_down)
        