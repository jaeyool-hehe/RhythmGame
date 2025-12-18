import pygame
import colors
import logic.game_state
import fonts

class VictoryOrLoseScreen:
    def __init__(self, screen_manager):
        self.screen_manager = screen_manager
        self.state: logic.game_state.GameState = screen_manager.state
        self.go_back_btn = pygame.Rect(550, 700, 100, 50)
        self._applied = False  # one-shot guard

    def update(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_s:
                self._applied = False
                self.screen_manager.switch("level_select")

            elif e.type == pygame.MOUSEBUTTONDOWN:
                if self.go_back_btn.collidepoint(e.pos):
                    self._applied = False
                    self.screen_manager.switch("level")

        if not self._applied and self.state.result == "Win":
            if self.state.selected_level == self.state.unlocked_until:
                self.state.unlocked_until += 1
            self._applied = True

    def draw(self, screen):
        screen.fill(colors.BLACK)

        text = "Victory" if self.state.result == "Win" else "Game over"
        txt = fonts.LOGO_FONT.render(text, True, colors.WHITE)
        screen.blit(txt, (500, 100))

        pygame.draw.rect(screen, colors.WHITE, self.go_back_btn, border_radius=20, width=2)
        screen.blit(
            fonts.BUTTON_FONT.render("Back", True, colors.WHITE),
            (self.go_back_btn.x + 23.5, self.go_back_btn.y + 15),
        )