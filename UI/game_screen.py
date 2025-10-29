import pygame
import Variables


class GameScreen:
   def __init__(self, screen_manager):
       self.screen_manager = screen_manager

       self.main_btn = pygame.Rect(1000, 700, 150, 50)

       self.game_menu_text_font = pygame.font.SysFont("gothicpixels", 50)
       self.font = pygame.font.SysFont("gothicpixels", 20)


   def update(self, events):
       for e in events:
           if e.type == pygame.KEYDOWN and e.key == pygame.K_m:
               self.screen_manager.switch("main")
           elif e.type == pygame.MOUSEBUTTONDOWN:
               if self.main_btn.collidepoint(e.pos):
                   self.screen_manager.switch("play")


   def draw(self, screen):
       screen.fill(Variables.BLACK)

       pygame.draw.rect(screen, Variables.WHITE, self.main_btn, border_radius=20, width=2)
       screen.blit(self.game_menu_text_font.render("Game Menu(Dummy ver)", True, Variables.WHITE), (450, 100))
       screen.blit(self.font.render("MainMenu", True, Variables.WHITE), (self.main_btn.x+19,self.main_btn.y+15))
