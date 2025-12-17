import pygame
import Variables
import logic.game_state

class GameScreen:
    # ---- Game rule constants (class-level) ----
    BOSS_MAX_HEALTH = {
        1: 200,
        2: 400,
        3: 600,
        4: 800,
        5: 1000,
    }

    def __init__(self, screen_manager):
        self.screen_manager = screen_manager
        self.state: logic.game_state.GameState = screen_manager.state

        # ---- UI layout (instance-level, mutable) ----
        self.main_btn = pygame.Rect(1000, 700, 150, 50)
        self.victory_btn = pygame.Rect(800, 700, 150, 50)
        self.game_over_btn = pygame.Rect(600, 700, 150, 50)
        self.pause_btn = pygame.Rect(25, 25, 150, 50)

        self.boss_box = pygame.Rect(800, 160, 250, 250)
        self.player_box = pygame.Rect(170, 160, 200, 250)
        self.boss_txt_box = pygame.Rect(800, 460, 250, 200)
        self.rhythm_box = pygame.Rect(385, 160, 400, 500)

        # ---- Health state (must exist before draw) ----
        self.boss_current_health = 0
        self.boss_health_bar_layout = pygame.Rect(800, 420, 250, 30)
        self.boss_health_rect = pygame.Rect(802, 422, 0, 26)

        self.player_health_bar_layout = pygame.Rect(170, 420, 200, 30)
        self.player_health_rect = pygame.Rect(172, 422, 196, 26)

        # ---- Load images ONCE ----
        self.boss_images = {
            1: pygame.transform.scale(
                pygame.image.load("assets/images/GeneralFrog/GeneralFrogState1.png"), (250, 250)
            ),
            2: pygame.transform.scale(
                pygame.image.load("assets/images/CommanderShrimp/CommanderShrimpState1.png"), (250, 250)
            ),
            3: pygame.transform.scale(
                pygame.image.load("assets/images/HornBull/HornBullState1.png"), (250, 250)
            ),
            4: pygame.transform.scale(
                pygame.image.load("assets/images/MagmaTurtle/MagmaTurtleState1.png"), (250, 250)
            ),
            5: pygame.transform.scale(
                pygame.image.load("assets/images/Crow/CrowState1.png"), (250, 250)
            ),
        }

        self.player_image = pygame.transform.scale(
            pygame.image.load("assets/images/Player/PlayerState1.png"), (250, 250)
        )

    # ---- Called once when entering the game screen ----
    def set_up_health(self):
        level = self.state.selected_level
        if level not in self.BOSS_MAX_HEALTH:
            return

        self.boss_current_health = self.BOSS_MAX_HEALTH[level]
        max_health = self.BOSS_MAX_HEALTH[level]

        bar_width = int(246 * self.boss_current_health / max_health)
        self.boss_health_rect.width = bar_width



    def update(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_m:
                self.screen_manager.switch("main")

            elif e.type == pygame.MOUSEBUTTONDOWN:
                if self.main_btn.collidepoint(e.pos):
                    self.screen_manager.switch("level")

                elif self.victory_btn.collidepoint(e.pos):
                    self.state.player_won()
                    self.screen_manager.switch("ending")

                elif self.game_over_btn.collidepoint(e.pos):
                    self.state.player_lost()
                    self.screen_manager.switch("ending")


                elif self.pause_btn.collidepoint(e.pos):
                    self.screen_manager.switch("pause")

    def draw(self, screen):
        screen.fill(Variables.BLACK)

        # ---- UI frames ----
        for rect in (
            self.main_btn,
            self.victory_btn,
            self.game_over_btn,
            self.pause_btn,
            self.boss_box,
            self.player_box,
            self.boss_txt_box,
            self.rhythm_box,
        ):
            pygame.draw.rect(screen, Variables.WHITE, rect, width=2)

        # ---- Health bars ----
        pygame.draw.rect(screen, Variables.RED, self.player_health_bar_layout)
        pygame.draw.rect(screen, Variables.WHITE, self.player_health_bar_layout, width=2)
        pygame.draw.rect(screen, Variables.YELLOW, self.player_health_rect)

        pygame.draw.rect(screen, Variables.RED, self.boss_health_bar_layout)
        pygame.draw.rect(screen, Variables.WHITE, self.boss_health_bar_layout, width=2)
        pygame.draw.rect(screen, Variables.YELLOW, self.boss_health_rect)

        # ---- Characters ----
        level = self.state.selected_level
        if level in self.boss_images:
            screen.blit(self.boss_images[level], (800, 150))
            screen.blit(self.player_image, (150, 150))
            screen.blit(
                Variables.LOGO_FONT.render(f"Level {level}", True, Variables.WHITE),
                (450, 100),
            )

        # ---- Text ----
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
