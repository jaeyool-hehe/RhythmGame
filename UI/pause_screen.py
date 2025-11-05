import pygame
import Variables


class PauseScreen:
    def __init__(self, screen_manager):
        self.screen_manager = screen_manager

        self.go_back_btn = pygame.Rect(500, 500, 100, 50)

        self.font = pygame.font.SysFont(Variables.BUTTON_FONT, 20)
        self.game_menu_text_font = pygame.font.SysFont(Variables.LOGO_FONT, 50)

    def update(self, screen, events):
        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_m:
                    self.screen_manager.switch("main")
            elif e.type == pygame.MOUSEBUTTONDOWN:
                if self.go_back_btn.collidepoint(e.pos):
                    self.screen_manager.switch("game")

    def draw(self, screen):
        screen.fill(Variables.BLACK)

        pygame.draw.rect(screen, Variables.WHITE, self.go_back_btn, border_radius=20, width=2)

        screen.blit(self.game_menu_text_font.render("Paused", True, Variables.WHITE), (450, 100))
        screen.blit(self.font.render("Go back", True, Variables.WHITE), (self.go_back_btn.x + 14, self.go_back_btn.x + 15))