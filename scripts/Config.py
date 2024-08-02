from pygame import image, transform, font, mixer, init
from Cropping import Cropping

class Constants:
    WIDTH_WINDOW = 900
    HEIGHT_WINDOW = 700
    TITLE_WINDOW = "Zvezdolet3000 on PyGame"

    GAME_NAME = "Zvezdolet3000"
    VERSION = "1.0"

    GAME_AUTHOR = "KocoyBot and ArFect"
    MUSIC_AND_SOUNDS_PLATFORM = "Zvukipro.com"
    SPECIAL_THANKS = "Keesac, Shandor_Shadow"
    
    FPS = 60

    SPEED_PULYA = 5
    SPEED_METEORITES = 7.5

    PLAYERS_LIVES = 5

class PATHS:
    IMAGES = "resources/images/"
    FONTS = "resources/fonts/"
    SOUNDS = "resources/sounds/"
    MUSIC = "resources/music/"

class Colors:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    PURPLE = (255, 0, 255)
    CYAN = (0, 255, 255)
    ORANGE = (255, 165, 0)
    PINK = (255, 192, 203)
    BROWN = (165, 42, 42)
    GRAY = (128, 128, 128)
    DARK_GRAY = (64, 64, 64)
    LIGHT_GRAY = (192, 192, 192)

class Images:
    ICON_WINDOW = image.load(PATHS.IMAGES + "game/zvezdolet.png")
    ZVEZDOLET_FOR_MAIN_MENU = transform.scale(image.load(PATHS.IMAGES + "game/zvezdolet.png"), (350, 470))
    ZVEZDOLET = transform.scale(image.load(PATHS.IMAGES + "game/zvezdolet.png"), (403//4, 505//4))
    BACKGROUND = transform.scale(image.load(PATHS.IMAGES + "game/background.jpg"), (900, 700))
    PULYA = transform.scale(image.load(PATHS.IMAGES + "game/pulya.png"), (25//5, 71/5))
    PLANETS = {
        1: image.load(PATHS.IMAGES + "game/planet_1.png"),
    }
    METEORITE = image.load(PATHS.IMAGES + "game/meteorite.png")

    BUTTONS = {
        "play": {
            "default": Cropping(image.load(PATHS.IMAGES + "main_menu/buttons/play_button.png"), 0, 0, 195, 74).crop(),
            "hover": Cropping(image.load(PATHS.IMAGES + "main_menu/buttons/play_button.png"), 0, 76, 195, 148).crop(),
            "click": Cropping(image.load(PATHS.IMAGES + "main_menu/buttons/play_button.png"), 0, 150, 195, 222).crop()
        },

        "options": {
            "default": Cropping(image.load(PATHS.IMAGES + "main_menu/buttons/options_button.png"), 0, 0, 301, 74).crop(),
            "hover": Cropping(image.load(PATHS.IMAGES + "main_menu/buttons/options_button.png"), 0, 76, 301, 150).crop(),
            "click": Cropping(image.load(PATHS.IMAGES + "main_menu/buttons/options_button.png"), 0, 152, 301, 225).crop()
        },

        "credits": {
            "default": Cropping(image.load(PATHS.IMAGES + "main_menu/buttons/credits_button.png"), 0, 0, 287, 72).crop(),
            "hover": Cropping(image.load(PATHS.IMAGES + "main_menu/buttons/credits_button.png"), 0, 74, 287, 148).crop(),
            "click": Cropping(image.load(PATHS.IMAGES + "main_menu/buttons/credits_button.png"), 0, 150, 287, 225).crop()
        },

        "exit": {
            "default": Cropping(image.load(PATHS.IMAGES + "main_menu/buttons/exit_button.png"), 0, 0, 178, 68).crop(),
            "hover": Cropping(image.load(PATHS.IMAGES + "main_menu/buttons/exit_button.png"), 0, 70, 178, 138).crop(),
            "click": Cropping(image.load(PATHS.IMAGES + "main_menu/buttons/exit_button.png"), 0, 140, 178, 207).crop()
        },

        "back": {
            "default": Cropping(image.load(PATHS.IMAGES + "main_menu/buttons/back_button.png"), 0, 0, 195, 74).crop(),
            "hover": Cropping(image.load(PATHS.IMAGES + "main_menu/buttons/back_button.png"), 0, 76, 195, 148).crop(),
            "click": Cropping(image.load(PATHS.IMAGES + "main_menu/buttons/back_button.png"), 0, 150, 195, 222).crop()
        },

        "main_menu": {
            "default": Cropping(image.load(PATHS.IMAGES + "main_menu/buttons/main_menu_button.png"), 0, 0, 195, 74).crop(),
            "hover": Cropping(image.load(PATHS.IMAGES + "main_menu/buttons/main_menu_button.png"), 0, 76, 195, 148).crop(),
            "click": Cropping(image.load(PATHS.IMAGES + "main_menu/buttons/main_menu_button.png"), 0, 150, 195, 222).crop()
        }
    }

class Fonts:
    def Zantroke(size: int) -> font.Font:
        return font.Font(PATHS.FONTS + "Zantroke.ttf", size)
    
class Sounds:
    mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
    init()
    BUTTON_CLICK = mixer.Sound(PATHS.SOUNDS + "UI/button_click.mp3")
    SHOOT = mixer.Sound(PATHS.SOUNDS + "game/shoot.mp3")

class Music:
    BACKGROUND_MAIN_MENU = mixer.Sound(PATHS.MUSIC + "background_main_menu.mp3")
    BACKGROUND_GAME = mixer.Sound(PATHS.MUSIC + "background_game.mp3")