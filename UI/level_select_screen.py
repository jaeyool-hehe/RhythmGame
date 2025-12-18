import pygame
import colors
import logic.game_state
import fonts


class LevelSelectScreen:
    def __init__(self, screen_manager):
        self.screen_manager = screen_manager
        self.state: logic.game_state.GameState = screen_manager.state

        # Buttons
        self.main_btn = pygame.Rect(1000, 700, 150, 50)
        self.continue_btn = pygame.Rect(800, 700, 150, 50)

        self.level_1_btn = pygame.Rect(200, 200, 150, 50)
        self.level_2_btn = pygame.Rect(200, 300, 150, 50)
        self.level_3_btn = pygame.Rect(200, 400, 150, 50)
        self.level_4_btn = pygame.Rect(200, 500, 150, 50)
        self.level_5_btn = pygame.Rect(200, 600, 150, 50)

    def update(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_m:
                self.screen_manager.switch("main")

            elif e.type == pygame.MOUSEBUTTONDOWN:
                if self.main_btn.collidepoint(e.pos):
                    self.screen_manager.switch("main")

                if self.level_1_btn.collidepoint(e.pos) and self.state.unlocked_until >= 1:
                    self.state.selected_level = 1

                if self.level_2_btn.collidepoint(e.pos) and self.state.unlocked_until >= 2:
                    self.state.selected_level = 2

                if self.level_3_btn.collidepoint(e.pos) and self.state.unlocked_until >= 3:
                    self.state.selected_level = 3

                if self.level_4_btn.collidepoint(e.pos) and self.state.unlocked_until >= 4:
                    self.state.selected_level = 4

                if self.level_5_btn.collidepoint(e.pos) and self.state.unlocked_until >= 5:
                    self.state.selected_level = 5

                if self.continue_btn.collidepoint(e.pos) and self.state.selected_level:
                    self.screen_manager.game.set_up_health()
                    self.screen_manager.switch("game")

    def draw(self, screen):
        screen.fill(colors.BLACK)

        # Draw main buttons
        pygame.draw.rect(screen, colors.WHITE, self.main_btn, border_radius=20, width=2)
        pygame.draw.rect(screen, colors.WHITE, self.continue_btn, border_radius=20, width=2)

        def level_color(level):
            if self.state.selected_level == level and self.state.unlocked_until >= level:
                return colors.HEALTH_BAR_BG
            elif self.state.unlocked_until >= level:
                return colors.WHITE
            else:
                return colors.GRAY

        # Draw level buttons
        pygame.draw.rect(screen, level_color(1), self.level_1_btn, border_radius=20, width=2)
        pygame.draw.rect(screen, level_color(2), self.level_2_btn, border_radius=20, width=2)
        pygame.draw.rect(screen, level_color(3), self.level_3_btn, border_radius=20, width=2)
        pygame.draw.rect(screen, level_color(4), self.level_4_btn, border_radius=20, width=2)
        pygame.draw.rect(screen, level_color(5), self.level_5_btn, border_radius=20, width=2)

        # Draw text
        screen.blit(fonts.BUTTON_FONT.render("Main Menu", True, colors.WHITE), (self.main_btn.x + 19, self.main_btn.y + 15))
        screen.blit(fonts.BUTTON_FONT.render("Continue", True, colors.WHITE), (self.continue_btn.x + 19, self.continue_btn.y + 15))
        screen.blit(fonts.LOGO_FONT.render("Select Level", True, colors.WHITE), (450, 100))
        screen.blit(fonts.BUTTON_FONT.render("Level 1", True, level_color(1)), (237, 215))
        screen.blit(fonts.BUTTON_FONT.render("Level 2", True, level_color(2)), (237, 315))
        screen.blit(fonts.BUTTON_FONT.render("Level 3", True, level_color(3)), (237, 415))
        screen.blit(fonts.BUTTON_FONT.render("Level 4", True, level_color(4)), (237, 515))
        screen.blit(fonts.BUTTON_FONT.render("Level 5", True, level_color(5)), (237, 615))
