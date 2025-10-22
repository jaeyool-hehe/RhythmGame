import pygame, sys

from UI.screen_manager import ScreenManager
from UI.main_menu_screen import MainMenu
from UI.game_screen import GameMenu
from UI.level_select_screen import LevelSelectScreen


pygame.init()
print(pygame.font.get_fonts())
screen = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()


# Create MenuBase (composition)
screen_manager = ScreenManager()

# Instantiate sub-menus with a reference to MenuBase
main_menu_screen = MainMenu(screen_manager)
game_screen = GameMenu(screen_manager)
level_select_screen = LevelSelectScreen(screen_manager)

# Set sub-menus in MenuBase
screen_manager.set_menus(main_menu_screen, level_select_screen, game_screen)


# Main loop
while True:
   events = pygame.event.get()
   for e in events:
       if e.type == pygame.QUIT:
           pygame.quit()
           sys.exit()

   screen_manager.current_screen_update(events)
   screen_manager.current_screen_draw(screen)


   pygame.display.flip()
   clock.tick(60)