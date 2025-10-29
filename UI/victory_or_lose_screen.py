import sys

import pygame
import Variables


class VictoryOrLoseScreen:
   def __init__(self, screen_manager):
       self.screen_manager = screen_manager
       self.go_back_btn = pygame.Rect(550, 700, 100, 50)
       self.main_text_font = pygame.font.SysFont("gothicpixels", 50)
       self.font = pygame.font.SysFont("gothicpixels", 20)
       self.txt = self.main_text_font.render("Victory", True, Variables.WHITE)


   def update(self, events):
       for e in events:
           if e.type == pygame.KEYDOWN:
               if e.key == pygame.K_s: self.screen_manager.switch("level_select")
           elif e.type == pygame.MOUSEBUTTONDOWN:
               if self.go_back_btn.collidepoint(e.pos):
                   self.screen_manager.switch("play")


   def draw(self, screen):
       screen.fill(Variables.BLACK)

       pygame.draw.rect(screen, Variables.WHITE, self.go_back_btn, border_radius=20, width=2)

       screen.blit(self.font.render("Back", True, Variables.WHITE), (self.go_back_btn.x + 23.5, self.go_back_btn.y + 15))
       if Variables.did_player_win_or_lose == "Win":
           self.txt = self.main_text_font.render("Victory", True, Variables.WHITE)
       elif Variables.did_player_win_or_lose == "Lose":
           self.txt = self.main_text_font.render("Gameover", True, Variables.WHITE)
       screen.blit(self.txt, (500, 100))