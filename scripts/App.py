import pygame
from Config import Constants, Images, Music, Sounds
from UI.Screens.MainMenuUI import MainMenuUI
from UI.Screens.CreditsUI import CreditsUI
from Game.Game import Game
from UI.Screens.GameOverUI import GameOverUI
import sys

class App:
    def __init__(self, size_window: tuple, title_window: str = "App on Pygame", icon_window: pygame.surface.Surface = None):
        pygame.init()

        self.window = pygame.display.set_mode(size_window)
        pygame.display.set_caption(title_window)
        if icon_window is not None: pygame.display.set_icon(icon_window)

        self.set_sound = True

        self.clock = pygame.time.Clock()

        self.mainMenu = MainMenuUI()
        self.credits = CreditsUI()
        self.game = Game()

        self.inMainMenu = False
        self.inGame = False
        self.inGameOver = False
        self.inOptions = False
        self.inCredits = False

        self.mouse_button_down = False

        self.planets_event = pygame.USEREVENT + 0
        self.meteorites_event = pygame.USEREVENT + 1

        pygame.time.set_timer(self.planets_event, 3000)
        pygame.time.set_timer(self.meteorites_event, 750)

    def __start_game(self):
        self.inMainMenu = False
        self.inGameOver = False
        self.inOptions = False
        self.inCredits = False
        self.inGame = True
        pygame.mouse.set_visible(False)
        if self.set_sound:
            Music.BACKGROUND_MAIN_MENU.stop()
            Music.BACKGROUND_GAME.play(-1)

    def __load_main_menu_music(self):
        if self.set_sound: 
            Music.BACKGROUND_GAME.stop()
            Music.BACKGROUND_MAIN_MENU.play(-1)

    def __show_main_menu(self):
        self.game.player.lives = Constants.PLAYERS_LIVES
        self.game.player.score = 0
        self.inMainMenu = True
        self.inGameOver = False
        self.inOptions = False
        self.inCredits = False
        self.inGame = False
        pygame.mouse.set_visible(True)

    def __show_options(self):
        self.inMainMenu = False
        self.inGameOver = False
        self.inOptions = True
        self.inCredits = False
        self.inGame = False

    def __show_game_over(self):
        self.inMainMenu = False
        self.inGameOver = True
        self.inOptions = False
        self.inCredits = False
        self.inGame = False
        pygame.mouse.set_visible(True)

    def __show_credits(self):
        self.inMainMenu = False
        self.inGameOver = False
        self.inOptions = False
        self.inGame = False
        self.inCredits = True

    def start_app(self) -> None:
        self.app = True
        print(Constants.GAME_NAME, Constants.VERSION, "by", Constants.GAME_AUTHOR, "is started...")
        self.__show_main_menu()
        self.__load_main_menu_music()
        self.__game_loop()

    def __game_loop(self) -> None:
        while self.app:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: self._stop_app()
                elif event.type == pygame.MOUSEBUTTONDOWN: self.mouse_button_down = True
                elif event.type == pygame.MOUSEBUTTONUP: 
                    self.mouse_button_down = False
                    if self.inMainMenu:
                        if self.mainMenu.button_play.button_mouse_button_up():
                            if self.set_sound: Sounds.BUTTON_CLICK.play()
                            self.game = Game()
                            self.__start_game()
                        elif self.mainMenu.button_options.button_mouse_button_up():
                            if self.set_sound: Sounds.BUTTON_CLICK.play()
                        elif self.mainMenu.button_credits.button_mouse_button_up():
                            if self.set_sound: Sounds.BUTTON_CLICK.play()
                            self.__show_credits()
                        elif self.mainMenu.button_exit.button_mouse_button_up():
                            if self.set_sound: Sounds.BUTTON_CLICK.play()
                            self._stop_app()
                    elif self.inCredits: 
                        if self.credits.button_back.button_mouse_button_up():
                            if self.set_sound: Sounds.BUTTON_CLICK.play()
                            self.__show_main_menu()
                    elif self.inGame:
                        self.game.create_pulya()
                        if self.set_sound:
                            Sounds.SHOOT.set_volume(0.1)
                            Sounds.SHOOT.play()
                    elif self.inGameOver: 
                        if self.gameOver.button_main_menu.button_mouse_button_up():
                            if self.set_sound: Sounds.BUTTON_CLICK.play()
                            self.__show_main_menu()
                            self.__load_main_menu_music()
                        

                elif event.type == self.planets_event:
                    if self.inGame: 
                        self.game.create_planet()

                elif event.type == self.meteorites_event:
                    if self.inGame:
                        self.game.create_meteorite()

            self.window.fill(0)

            if self.inMainMenu: self.mainMenu.load(self.window, self.mouse_button_down)

            elif self.inGame: 
                self.game.load(self.window, self.set_sound)
                if self.game.player.check_lives(): 
                    self.__show_game_over()
                    self.gameOver = GameOverUI(self.game.player)

            elif self.inCredits: self.credits.load(self.window, self.mouse_button_down)

            elif self.inGameOver:
                self.gameOver.load(self.window, self.mouse_button_down)
            
            self.clock.tick(Constants.FPS)
            pygame.display.update()

    def _stop_app(self) -> None:
        self.app = False
        print(Constants.GAME_NAME, Constants.VERSION, "by", Constants.GAME_AUTHOR, "is stopped...")
        pygame.quit()
        sys.exit()