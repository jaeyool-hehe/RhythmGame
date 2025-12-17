import sys
import pygame
import Variables


class MainMenu:
   def __init__(self, screen_manager):
       self.screen_manager = screen_manager
       self.play_btn = pygame.Rect(550, 200, 100, 50)
       self.exit_btn = pygame.Rect(550, 300, 100, 50)


   def update(self, events):
       for e in events:
           if e.type == pygame.KEYDOWN:
               if e.key == pygame.K_s: self.screen_manager.switch("level")
           elif e.type == pygame.MOUSEBUTTONDOWN:
               if self.play_btn.collidepoint(e.pos):
                   self.screen_manager.switch("level")
               if self.exit_btn.collidepoint(e.pos):
                   sys.exit()


   def draw(self, screen):
       screen.fill(Variables.BLACK)
       txt = Variables.LOGO_FONT.render("PULSEBOUND", True, Variables.WHITE)
       screen.blit(txt, (400, 100))
       pygame.draw.rect(screen, Variables.WHITE, self.play_btn, border_radius=20, width=2)
       pygame.draw.rect(screen, Variables.WHITE, self.exit_btn, border_radius=20, width=2)
       screen.blit(Variables.BUTTON_FONT.render("Play", True, Variables.WHITE), (self.play_btn.x + 23.5, self.play_btn.y + 15))
       screen.blit(Variables.BUTTON_FONT.render("Exit", True, Variables.WHITE), (self.exit_btn.x + 25.75, self.exit_btn.y + 15))