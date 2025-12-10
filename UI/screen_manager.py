import Variables
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
        if name == "level":
            Variables.selected_level = None
            self.level_select.level_1_button_color = Variables.WHITE
            self.level_select.level_2_button_color = Variables.WHITE
            self.level_select.level_3_button_color = Variables.WHITE
            self.level_select.level_4_button_color = Variables.WHITE
            self.level_select.level_5_button_color = Variables.WHITE
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

    def current_screen_update(self, events):
        self.current.update(events)

    def current_screen_draw(self, screen):
        self.current.draw(screen)
