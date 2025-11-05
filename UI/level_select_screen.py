import pygame
import Variables


class LevelSelectScreen:
    def __init__(self, screen_manager):
        self.screen_manager = screen_manager
        self.button_color = Variables.WHITE
        self.main_btn = pygame.Rect(1000, 700, 150, 50)
        self.continue_button = pygame.Rect(800, 700, 150, 50)
        self.level_1_out_line_button = pygame.Rect(200, 200, 150, 50)

        self.game_menu_text_font = pygame.font.SysFont(Variables.LOGO_FONT, 50)
        self.font = pygame.font.SysFont(Variables.BUTTON_FONT, 20)

    def update(self, screen, events):
        for e in events:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_m:
                self.screen_manager.switch("main")

            elif e.type == pygame.MOUSEBUTTONDOWN:
                if self.main_btn.collidepoint(e.pos):
                    self.screen_manager.switch("main")

                if self.level_1_out_line_button.collidepoint(e.pos):
                    Variables.level = 1

                if self.continue_button.collidepoint(e.pos):
                    self.screen_manager.switch("game")

                if self.level_1_out_line_button.collidepoint(e.pos):
                    self.button_color = Variables.RED
    def draw(self, screen):
        screen.fill(Variables.BLACK)

        pygame.draw.rect(screen, Variables.WHITE, self.main_btn, border_radius=20, width=2)
        pygame.draw.rect(screen, Variables.WHITE, self.continue_button, border_radius=20, width=2)
        pygame.draw.rect(screen, self.button_color, self.level_1_out_line_button, border_radius=20, width=2)

        screen.blit(self.font.render("Main Menu", True, Variables.WHITE), (self.main_btn.x + 19, self.main_btn.y + 15))
        screen.blit(self.font.render("Continue", True, Variables.WHITE),
                    (self.continue_button.x + 19, self.continue_button.y + 15))
        screen.blit(self.game_menu_text_font.render("Select Level", True, Variables.WHITE), (450, 100))
        screen.blit(self.font.render("Level 1", True, Variables.WHITE), (237, 215))