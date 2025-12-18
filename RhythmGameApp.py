import pygame, sys

import UI.screen_manager
import logic.game_state
import fonts
import images

pygame.init()
fonts.initFonts()
images.load_boss_images()
images.load_player_images()


print(pygame.font.get_fonts())
screen = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()

# Create MenuBase (composition)
state = logic.game_state.GameState()
screen_manager = UI.screen_manager.ScreenManager(state)



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
