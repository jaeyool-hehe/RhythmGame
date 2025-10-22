import sys

import pygame


class MainMenu:
   def __init__(self, screen_manager):
       self.screen_manager = screen_manager
       self.play_btn = pygame.Rect(50, 200, 100, 25)
       self.exit_btn = pygame.Rect(50, 250, 100, 25)
       self.main_text_font = pygame.font.SysFont("gothicpixels", 50)
       self.font = pygame.font.SysFont("gothicpixels", 20)


   def update(self, events):
       for e in events:
           if e.type == pygame.KEYDOWN:
               if e.key == pygame.K_s: self.screen_manager.switch("play")
           elif e.type == pygame.MOUSEBUTTONDOWN:
               if self.play_btn.collidepoint(e.pos):
                   self.screen_manager.switch("play")
               if self.exit_btn.collidepoint(e.pos):
                   sys.exit()


   def draw(self, screen):
       screen.fill((0, 0, 0))
       txt = self.main_text_font.render("PULSEBOUND", True, (255,255,255))
       screen.blit(txt, (50, 100))
       pygame.draw.rect(screen, (100,100,255), self.play_btn, border_radius=20)
       pygame.draw.rect(screen, (100,255,100), self.exit_btn, border_radius=20)
       screen.blit(self.font.render("Play", True, (255,255,255)), (self.play_btn.x + 23.5, self.play_btn.y + 5))
       screen.blit(self.font.render("Exit", True, (255,255,255)), (self.exit_btn.x + 23.5, self.exit_btn.y + 5))