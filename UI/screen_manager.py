import colors
import UI.main_menu_screen
import UI.game_screen
import UI.level_select_screen
import UI.victory_or_lose_screen
import UI.pause_screen


class ScreenManager:
    def __init__(self, state):
        self.state = state
        # Compose the sub-menus
        self.main = UI.main_menu_screen.MainMenu(self)
        self.game = UI.game_screen.GameScreen(self)
        self.level_select = UI.level_select_screen.LevelSelectScreen(self)
        self.victory_or_lose = UI.victory_or_lose_screen.VictoryOrLoseScreen(self)
        self.pause = UI.pause_screen.PauseScreen(self)
        self.current = self.main


    def switch(self, name):
        if name == "level":
            colors.selected_level = None
            self.level_select.level_1_button_color = colors.WHITE
            self.level_select.level_2_button_color = colors.WHITE
            self.level_select.level_3_button_color = colors.WHITE
            self.level_select.level_4_button_color = colors.WHITE
            self.level_select.level_5_button_color = colors.WHITE
            self.current = self.level_select
        elif name == "main":
            self.current = self.main
        elif name == "game":
            self.current = self.game
        elif name == "ending":
            self.current = self.victory_or_lose
        elif name == "pause":
            self.current = self.pause
        else:
            raise Exception("This screen doesn't exist")

    def current_screen_update(self, events):
        self.current.update(events)

    def current_screen_draw(self, screen):
        self.current.draw(screen)