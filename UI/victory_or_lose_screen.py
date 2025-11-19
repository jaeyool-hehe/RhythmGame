import sys

import pygame
import Variables


class VictoryOrLoseScreen:
    def __init__(self, screen_manager):
        self.screen_manager = screen_manager

        self.go_back_btn = pygame.Rect(550, 700, 100, 50)

    def update(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_s: self.screen_manager.switch("level_select")

            elif e.type == pygame.MOUSEBUTTONDOWN:
                if self.go_back_btn.collidepoint(e.pos):
                    self.screen_manager.switch("level")

        if Variables.did_player_win_or_lose == "Win":
            if Variables.selected_level == 1 and Variables.unlocked_until_this_level == 1:
                Variables.unlocked_until_this_level = 2
            elif Variables.selected_level == 2 and Variables.unlocked_until_this_level == 2:
                Variables.unlocked_until_this_level = 3
            elif Variables.selected_level == 3 and Variables.unlocked_until_this_level == 3:
                Variables.unlocked_until_this_level = 4
            elif Variables.selected_level == 4 and Variables.unlocked_until_this_level == 4:
                Variables.unlocked_until_this_level = 5

    def draw(self, screen):
        screen.fill(Variables.BLACK)

        if Variables.did_player_win_or_lose == "Win":
            self.txt = Variables.LOGO_FONT.render("Victory", True, Variables.WHITE)
        elif Variables.did_player_win_or_lose == "Lose":
            self.txt = Variables.LOGO_FONT.render("Gameover", True, Variables.WHITE)
        screen.blit(self.txt, (500, 100))

        # Back button
        pygame.draw.rect(screen, Variables.WHITE, self.go_back_btn, border_radius=20, width=2)
        screen.blit(Variables.BUTTON_FONT.render("Back", True, Variables.WHITE),
                    (self.go_back_btn.x + 23.5, self.go_back_btn.y + 15))