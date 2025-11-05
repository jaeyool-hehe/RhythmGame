import pygame
import Variables


class GameScreen:
    def __init__(self, screen_manager):
        self.screen_manager = screen_manager

        self.main_btn = pygame.Rect(1000, 700, 150, 50)
        self.victory_btn = pygame.Rect(800, 700, 150, 50)
        self.game_over_btn = pygame.Rect(600, 700, 150, 50)
        self.pause_btn = pygame.Rect(25, 25, 150, 50)

        self.game_menu_text_font = pygame.font.SysFont(Variables.LOGO_FONT, 50)
        self.font = pygame.font.SysFont(Variables.BUTTON_FONT, 20)

    def update(self, screen, events):
        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_m:
                    self.screen_manager.switch("main")

            elif e.type == pygame.MOUSEBUTTONDOWN:
                if self.main_btn.collidepoint(e.pos):
                    self.screen_manager.switch("play")
                if self.victory_btn.collidepoint(e.pos):
                    Variables.did_player_win_or_lose = "Win"
                    self.screen_manager.switch("Ending")
                if self.game_over_btn.collidepoint(e.pos):
                    Variables.did_player_win_or_lose = "Lose"
                    self.screen_manager.switch("Ending")
                if self.pause_btn.collidepoint(e.pos):
                    self.screen_manager.switch("pause")

    def draw(self, screen):
        screen.fill(Variables.BLACK)

        pygame.draw.rect(screen, Variables.WHITE, self.main_btn, border_radius=20, width=2)
        pygame.draw.rect(screen, Variables.WHITE, self.victory_btn, border_radius=20, width=2)
        pygame.draw.rect(screen, Variables.WHITE, self.game_over_btn, border_radius=20, width=2)
        pygame.draw.rect(screen, Variables.WHITE, self.pause_btn, border_radius=20, width=2)


        if Variables.level == 1:
            screen.blit(self.game_menu_text_font.render("Level 1", True, Variables.WHITE), (450, 100))
        if Variables.level == 2:
            screen.blit(self.game_menu_text_font.render("Level 2", True, Variables.WHITE), (450, 100))
        if Variables.level == 3:
            screen.blit(self.game_menu_text_font.render("Level 3", True, Variables.WHITE), (450, 100))
        if Variables.level == 4:
            screen.blit(self.game_menu_text_font.render("Level 4", True, Variables.WHITE), (450, 100))
        if Variables.level == 5:
            screen.blit(self.game_menu_text_font.render("Level 5", True, Variables.WHITE), (450, 100))

        screen.blit(self.font.render(" ll pause", True, Variables.WHITE), (self.pause_btn.x + 19, self.pause_btn.y + 15))
        screen.blit(self.font.render("Win", True, Variables.WHITE), (self.victory_btn.x + 19, self.victory_btn.y + 15))
        screen.blit(self.font.render("Lose", True, Variables.WHITE), (self.game_over_btn.x + 19, self.game_over_btn.y + 15))
        screen.blit(self.font.render("Back", True, Variables.WHITE), (self.main_btn.x + 19, self.main_btn.y + 15))