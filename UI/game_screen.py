import pygame
import Variables


class GameScreen:
    def __init__(self, screen_manager):
        self.screen_manager = screen_manager

        self.main_btn = pygame.Rect(1000, 700, 150, 50)
        self.victory_btn = pygame.Rect(800, 700, 150, 50)
        self.game_over_btn = pygame.Rect(600, 700, 150, 50)
        self.pause_btn = pygame.Rect(25, 25, 150, 50)
        self.boss_box = pygame.Rect(800, 160, 250, 250)
        self.player_box = pygame.Rect(170, 160, 200, 250)
        self.main_box = pygame.Rect(0, 0, 0, 0)
        self.boss_txt_box = pygame.Rect(800, 460, 250, 200)
        self.rhythm_box = pygame.Rect(385, 160, 400, 500)

        # self.first_boss_health_bar_decreasing_rate?
        self.FIRST_BOSS_MAX_HEALTH = 200
        self.SECOND_BOSS_MAX_HEALTH = 400
        self.THIRD_BOSS_MAX_HEALTH = 600
        self.FOURTH_BOSS_MAX_HEALTH = 800
        self.FIFTH_BOSS_MAX_HEALTH = 1000

    # it runs after you select the level
    def set_up_health(self):
        health_bar_length = 0
        if Variables.selected_level == 1:
            boss_current_health = self.FIRST_BOSS_MAX_HEALTH
            health_bar_length = 246 / self.FIRST_BOSS_MAX_HEALTH * self.boss_current_health
        elif Variables.selected_level == 2:
            boss_current_health = self.SECOND_BOSS_MAX_HEALTH
            health_bar_length = 246 / self.SECOND_BOSS_MAX_HEALTH * self.boss_current_health
        elif Variables.selected_level == 3:
            boss_current_health = self.THIRD_BOSS_MAX_HEALTH
            health_bar_length = 246 / self.THIRD_BOSS_MAX_HEALTH * self.boss_current_health
        elif Variables.selected_level == 4:
            boss_current_health = self.FOURTH_BOSS_MAX_HEALTH
            health_bar_length = 246 / self.FOURTH_BOSS_MAX_HEALTH * self.boss_current_health
        elif Variables.selected_level == 5:
            boss_current_health = self.FIFTH_BOSS_MAX_HEALTH
            health_bar_length = 246 / self.FIFTH_BOSS_MAX_HEALTH * self.boss_current_health

        self.boss_health_bar_layout = pygame.Rect(800, 420, 250, 30)
        self.boss_health_rect = pygame.Rect(802, 422, health_bar_length, 26)

        self.player_health_bar_layout = pygame.Rect(170, 420, 200, 30)
        self.player_health_rect = pygame.Rect(172, 422, 196, 26)


def update(self, events):
    for e in events:
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_m:
                self.screen_manager.switch("main")

        elif e.type == pygame.MOUSEBUTTONDOWN:
            if self.main_btn.collidepoint(e.pos):
                self.screen_manager.switch("level")

            if self.victory_btn.collidepoint(e.pos):
                Variables.did_player_win_or_lose = "Win"
                self.screen_manager.switch("Ending")

            if self.game_over_btn.collidepoint(e.pos):
                Variables.did_player_win_or_lose = "Lose"
                self.screen_manager.switch("Ending")

            if self.pause_btn.collidepoint(e.pos):
                self.screen_manager.switch("pause")


def draw(self, screen):
    # Filling the screen black
    screen.fill(Variables.BLACK)

    # Drawing btn
    pygame.draw.rect(screen, Variables.WHITE, self.main_btn, border_radius=20, width=2)
    pygame.draw.rect(screen, Variables.WHITE, self.victory_btn, border_radius=20, width=2)
    pygame.draw.rect(screen, Variables.WHITE, self.game_over_btn, border_radius=20, width=2)
    pygame.draw.rect(screen, Variables.WHITE, self.pause_btn, border_radius=20, width=2)
    pygame.draw.rect(screen, Variables.WHITE, self.boss_txt_box, width=2)
    pygame.draw.rect(screen, Variables.WHITE, self.rhythm_box, width=2)

    pygame.draw.rect(screen, Variables.RED, self.player_health_bar_layout)
    pygame.draw.rect(screen, Variables.WHITE, self.player_health_bar_layout, width=2)
    pygame.draw.rect(screen, Variables.YELLOW, self.player_health_rect)

    pygame.draw.rect(screen, Variables.RED, self.boss_health_bar_layout)
    pygame.draw.rect(screen, Variables.WHITE, self.boss_health_bar_layout, width=2)
    pygame.draw.rect(screen, Variables.YELLOW, self.boss_health_rect)

    # Managing level txt
    if Variables.selected_level == 1:
        general_frog_state_1_image = pygame.image.load("assets/images/GeneralFrog/GeneralFrogState1.png")
        general_frog_state_1_image = pygame.transform.scale(general_frog_state_1_image, (250, 250))
        player_state_1_image = pygame.image.load("assets/images/Player/PlayerState1.png")
        player_state_1_image = pygame.transform.scale(player_state_1_image, (250, 250))

        pygame.draw.rect(screen, Variables.WHITE, self.boss_box, width=2)
        pygame.draw.rect(screen, Variables.WHITE, self.player_box, width=2)
        screen.blit(general_frog_state_1_image, (800, 150))
        screen.blit(player_state_1_image, (150, 150))
        screen.blit(Variables.LOGO_FONT.render("Level 1", True, Variables.WHITE), (450, 100))

    if Variables.selected_level == 2:
        commander_shrimp_state_1_image = pygame.image.load("assets/images/CommanderShrimp/CommanderShrimpState1.png")
        commander_shrimp_state_1_image = pygame.transform.scale(commander_shrimp_state_1_image, (250, 250))
        player_state_1_image = pygame.image.load("assets/images/Player/PlayerState1.png")
        player_state_1_image = pygame.transform.scale(player_state_1_image, (250, 250))

        screen.blit(commander_shrimp_state_1_image, (800, 150))
        pygame.draw.rect(screen, Variables.WHITE, self.boss_box, width=2)
        pygame.draw.rect(screen, Variables.WHITE, self.player_box, width=2)
        screen.blit(player_state_1_image, (150, 150))
        screen.blit(Variables.LOGO_FONT.render("Level 2", True, Variables.WHITE), (450, 100))

    if Variables.selected_level == 3:
        horn_bull_state_1_image = pygame.image.load("assets/images/HornBull/HornBullState1.png")
        horn_bull_state_1_image = pygame.transform.scale(horn_bull_state_1_image, (250, 250))
        player_state_1_image = pygame.image.load("assets/images/Player/PlayerState1.png")
        player_state_1_image = pygame.transform.scale(player_state_1_image, (250, 250))

        screen.blit(horn_bull_state_1_image, (800, 150))
        pygame.draw.rect(screen, Variables.WHITE, self.boss_box, width=2)
        pygame.draw.rect(screen, Variables.WHITE, self.player_box, width=2)
        screen.blit(player_state_1_image, (150, 150))
        screen.blit(Variables.LOGO_FONT.render("Level 3", True, Variables.WHITE), (450, 100))

    if Variables.selected_level == 4:
        magma_turtle_state_1_image = pygame.image.load("assets/images/MagmaTurtle/MagmaTurtleState1.png")
        magma_turtle_state_1_image = pygame.transform.scale(magma_turtle_state_1_image, (250, 250))
        player_state_1_image = pygame.image.load("assets/images/Player/PlayerState1.png")
        player_state_1_image = pygame.transform.scale(player_state_1_image, (250, 250))

        screen.blit(magma_turtle_state_1_image, (800, 200))
        pygame.draw.rect(screen, Variables.WHITE, self.boss_box, width=2)
        pygame.draw.rect(screen, Variables.WHITE, self.player_box, width=2)
        screen.blit(player_state_1_image, (150, 150))
        screen.blit(Variables.LOGO_FONT.render("Level 4", True, Variables.WHITE), (450, 100))

    if Variables.selected_level == 5:
        crow_state_1_image = pygame.image.load("assets/images/Crow/CrowState1.png")
        crow_state_1_image = pygame.transform.scale(crow_state_1_image, (250, 250))
        player_state_1_image = pygame.image.load("assets/images/Player/PlayerState1.png")
        player_state_1_image = pygame.transform.scale(player_state_1_image, (250, 250))

        screen.blit(crow_state_1_image, (800, 150))
        pygame.draw.rect(screen, Variables.WHITE, self.boss_box, width=2)
        pygame.draw.rect(screen, Variables.WHITE, self.player_box, width=2)
        screen.blit(player_state_1_image, (150, 150))
        screen.blit(Variables.LOGO_FONT.render("Level 5", True, Variables.WHITE), (450, 100))

    # Displaying txt
    screen.blit(Variables.BUTTON_FONT.render("II Pause", True, Variables.WHITE),
                (self.pause_btn.x + 19, self.pause_btn.y + 15))
    screen.blit(Variables.BUTTON_FONT.render("Win", True, Variables.WHITE),
                (self.victory_btn.x + 19, self.victory_btn.y + 15))
    screen.blit(Variables.BUTTON_FONT.render("Lose", True, Variables.WHITE),
                (self.game_over_btn.x + 19, self.game_over_btn.y + 15))
    screen.blit(Variables.BUTTON_FONT.render("Back", True, Variables.WHITE),
                (self.main_btn.x + 19, self.main_btn.y + 15))
    screen.blit(Variables.BUTTON_FONT.render("HarHarHar...", True, Variables.WHITE),
                (self.boss_txt_box.x + 19, self.boss_txt_box.y + 15))
