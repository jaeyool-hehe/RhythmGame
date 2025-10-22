import pygame


class GameMenu:
   def __init__(self, screen_manager):
       self.screen_manager = screen_manager
       self.main_btn = pygame.Rect(50, 200, 100, 25)
       self.game_menu_text_font = pygame.font.SysFont(None, 50)
       self.font = pygame.font.SysFont(None, 20)


   def update(self, events):
       for e in events:
           if e.type == pygame.KEYDOWN and e.key == pygame.K_m:
               self.screen_manager.switch("main")
           elif e.type == pygame.MOUSEBUTTONDOWN:
               if self.main_btn.collidepoint(e.pos):
                   self.screen_manager.switch("main")


   def draw(self, screen):
       screen.fill((50, 150, 50))
       screen.blit(self.game_menu_text_font.render("Game Menu", True, (255, 255, 255)), (50, 150))
       pygame.draw.rect(screen, (200, 255, 200), self.main_btn, border_radius=20)
       screen.blit(self.font.render("Main Menu", True, (0, 0, 0)), (self.main_btn.x+19,self.main_btn.y+5))