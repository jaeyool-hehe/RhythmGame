class ScreenManager:
    def __init__(self):
        # Compose the sub-menus
        self.main = None
        self.game = None
        self.current = None
        self.level_select = None
        self.game = None
        self.pause = None

    def set_menus(self, main, level_select, game, victory_or_end, pause):
        self.main = main
        self.level_select = level_select
        self.game = game
        self.victory_or_end = victory_or_end
        self.pause = pause
        # self.current = main  # default: start with main menu
        self.current = main  # start with main menu

    def switch(self, name):
        if name == "play":
            self.current = self.level_select
        elif name == "main":
            self.current = self.main
        elif name == "game":
            self.current = self.game
        elif name == "Ending":
            self.current = self.victory_or_end
        elif name == "pause":
            self.current = self.pause
        else:
            raise Exception("This screen doesn't exist")

    def current_screen_update(self, screen, events):
        self.current.update(screen, events)

    def current_screen_draw(self, screen):
        self.current.draw(screen)
