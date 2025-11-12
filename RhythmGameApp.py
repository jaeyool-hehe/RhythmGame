import pygame, sys

import Variables
from UI.screen_manager import ScreenManager


pygame.init()
Variables.initFonts()


print(pygame.font.get_fonts())
screen = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()

# Create MenuBase (composition)
screen_manager = ScreenManager()



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
