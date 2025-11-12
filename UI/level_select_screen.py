import pygame
import Variables


class LevelSelectScreen:
    def __init__(self, screen_manager):
        self.screen_manager = screen_manager

        self.main_btn = pygame.Rect(1000, 700, 150, 50)
        self.continue_button = pygame.Rect(800, 700, 150, 50)

        self.level_1_out_line_button = pygame.Rect(200, 200, 150, 50)
        self.level_2_out_line_button = pygame.Rect(200, 300, 150, 50)
        self.level_3_out_line_button = pygame.Rect(200, 400, 150, 50)
        self.level_4_out_line_button = pygame.Rect(200, 500, 150, 50)
        self.level_5_out_line_button = pygame.Rect(200, 600, 150, 50)



    def update(self, events):


        for e in events:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_m:
                self.screen_manager.switch("main")

            elif e.type == pygame.MOUSEBUTTONDOWN:
                if self.main_btn.collidepoint(e.pos):
                    self.screen_manager.switch("main")

                if self.level_1_out_line_button.collidepoint(e.pos):
                    Variables.selected_level = 1
                if self.level_2_out_line_button.collidepoint(e.pos):
                    Variables.selected_level = 2
                if self.level_3_out_line_button.collidepoint(e.pos):
                    Variables.selected_level = 3

                if self.level_4_out_line_button.collidepoint(e.pos):
                    Variables.selected_level = 4

                if self.level_5_out_line_button.collidepoint(e.pos):
                    Variables.selected_level = 5

                if self.continue_button.collidepoint(e.pos) and Variables.selected_level:
                    self.screen_manager.switch("game")





    def draw(self, screen):
        screen.fill(Variables.BLACK)

        pygame.draw.rect(screen, Variables.WHITE, self.main_btn, border_radius=20, width=2)
        pygame.draw.rect(screen, Variables.WHITE, self.continue_button, border_radius=20, width=2)

        # TODO MAKE IT SO YOU CAN'T SELECT GRAYED OUT BUTTONS
        def get_level_color(level):
            if Variables.selected_level == level:
                return Variables.RED
            elif Variables.unlocked_until_this_level >= level:
                return Variables.WHITE
            else:
                return Variables.GRAY

        color1 = get_level_color(1)
        color2 = get_level_color(2)
        color3 = get_level_color(3)
        color4 = get_level_color(4)
        color5 = get_level_color(5)


        pygame.draw.rect(screen, color1, self.level_1_out_line_button, border_radius=20, width=2)
        pygame.draw.rect(screen, color2, self.level_2_out_line_button, border_radius=20, width=2)
        pygame.draw.rect(screen, color3, self.level_3_out_line_button, border_radius=20, width=2)
        pygame.draw.rect(screen, color4, self.level_4_out_line_button, border_radius=20, width=2)
        pygame.draw.rect(screen, color5, self.level_5_out_line_button, border_radius=20, width=2)

        screen.blit(Variables.BUTTON_FONT.render("Main Menu", True, Variables.WHITE), (self.main_btn.x + 19, self.main_btn.y + 15))
        screen.blit(Variables.BUTTON_FONT.render("Continue", True, Variables.WHITE), (self.continue_button.x + 19, self.continue_button.y + 15))

        screen.blit(Variables.LOGO_FONT.render("Select Level", True, Variables.WHITE), (450, 100))
        screen.blit(Variables.BUTTON_FONT.render("Level 1", True, self.level_1_button_color), (237, 215))
        screen.blit(Variables.BUTTON_FONT.render("Level 2", True, self.level_2_button_color), (237, 315))
        screen.blit(Variables.BUTTON_FONT.render("Level 3", True, self.level_3_button_color), (237, 415))
        screen.blit(Variables.BUTTON_FONT.render("Level 4", True, self.level_4_button_color), (237, 515))
        screen.blit(Variables.BUTTON_FONT.render("Level 5", True, self.level_5_button_color), (237, 615))