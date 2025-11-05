
from UI.main_menu_screen import MainMenu
from UI.game_screen import GameScreen
from UI.level_select_screen import LevelSelectScreen
from UI.victory_or_lose_screen import VictoryOrLoseScreen
from UI.pause_screen import PauseScreen

class ScreenManager:
    def __init__(self):
        # Compose the sub-menus
        self.main = MainMenu(self)
        self.game = GameScreen(self)
        self.level_select = LevelSelectScreen(self)
        self.victory_or_lose = VictoryOrLoseScreen(self)
        self.pause = PauseScreen(self)
        self.current = self.main


    def switch(self, name):
        if name == "play":
            self.current = self.level_select
        elif name == "main":
            self.current = self.main
        elif name == "game":
            self.current = self.game
        elif name == "Ending":
            self.current = self.victory_or_lose
        elif name == "pause":
            self.current = self.pause
        else:
            raise Exception("This screen doesn't exist")

    def current_screen_update(self, screen, events):
        self.current.update(screen, events)

    def current_screen_draw(self, screen):
        self.current.draw(screen)
