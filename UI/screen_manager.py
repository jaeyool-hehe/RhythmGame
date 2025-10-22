class ScreenManager:
   def __init__(self):
       # Compose the sub-menus
       self.main = None
       self.game = None
       self.current = None
       self.level_select = None


   def set_menus(self, main, level_select, game):
       self.main = main
       self.level_select = level_select
       self.game = game
       self.current = main  # start with main menu


   def switch(self, name):
       if name == "play": self.current = self.level_select
       elif name == "main": self.current = self.main
       elif name == "game": self.current = self.game


   def current_screen_update(self, events):
       self.current.update(events)


   def current_screen_draw(self, screen):
       self.current.draw(screen)
