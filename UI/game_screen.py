import pygame
import colors
import logic.game_state
import fonts
import images

class GameScreen:
    # ---- Game rule constants (class-level) ----
    BOSS_MAX_HEALTH = {
        1: 200,
        2: 400,
        3: 600,
        4: 800,
        5: 1000,
    }
    PLAYER_MAX_HEALTH = 100
    BOSS_HEALTH_BAR_LENGTH_PIXELS = 250
    PLAYER_HEALTH_BAR_LENGTH_PIXELS = 200

    def __init__(self, screen_manager):
        self.screen_manager = screen_manager
        self.state: logic.game_state.GameState = screen_manager.state

        # ---- UI layout (instance-level, mutable) ----
        self.main_btn_rect = pygame.Rect(1000, 700, 150, 50)
        self.victory_btn_rect = pygame.Rect(800, 700, 150, 50)
        self.game_over_btn_rect = pygame.Rect(600, 700, 150, 50)
        self.pause_btn_rect = pygame.Rect(25, 25, 150, 50)

        self.boss_box_rect = pygame.Rect(800, 160, 250, 250)
        self.player_box_rect = pygame.Rect(170, 160, 200, 250)
        self.boss_txt_box_rect = pygame.Rect(800, 460, 250, 200)
        self.rhythm_box_rect = pygame.Rect(385, 160, 400, 500)

        # ---- Health state (must exist before draw) ----
        self.player_current_health = -1
        # it is drawn as red bar with white border
        self.player_health_bar_frame_rect = pygame.Rect(170, 420, GameScreen.PLAYER_HEALTH_BAR_LENGTH_PIXELS, 30)

        self.boss_current_health = -1 # indeterminate until level is chosen
        # it is drawn as red bar with white border
        self.boss_health_bar_frame_rect = pygame.Rect(800, 420, GameScreen.BOSS_HEALTH_BAR_LENGTH_PIXELS, 30)




    # you would use @property for computed fields
    # you want to have dependent fields to be computed because of single source of truth
    @property
    def player_current_health_rect(self):
        width = int(self.player_current_health / GameScreen.PLAYER_MAX_HEALTH * GameScreen.PLAYER_HEALTH_BAR_LENGTH_PIXELS)
        return pygame.Rect(170, 420, width, 30)

    @property
    def boss_current_health_rect(self):
        level = self.state.selected_level
        width = int(self.boss_current_health / GameScreen.BOSS_MAX_HEALTH[level] * GameScreen.BOSS_HEALTH_BAR_LENGTH_PIXELS)
        return pygame.Rect(800, 420, width, 30)

    # ---- Called once when entering the game screen ----
    def set_up_health(self):
        level = self.state.selected_level
        if level not in GameScreen.BOSS_MAX_HEALTH:
            raise Exception("There should be 5 buttons in level select screen and 5 pairs in BOSS_MAX_HEALTH dictionary")

        self.boss_current_health = GameScreen.BOSS_MAX_HEALTH[level]
        self.player_current_health = GameScreen.PLAYER_MAX_HEALTH
        self.boss_current_health = 50
        self.player_current_health = 50





    def update(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_m:
                self.screen_manager.switch("main")

            elif e.type == pygame.MOUSEBUTTONDOWN:
                if self.main_btn_rect.collidepoint(e.pos):
                    self.screen_manager.switch("level")
                elif self.victory_btn_rect.collidepoint(e.pos):
                    self.state.player_won()
                    self.screen_manager.switch("ending")
                elif self.game_over_btn_rect.collidepoint(e.pos):
                    self.state.player_lost()
                    self.screen_manager.switch("ending")
                elif self.pause_btn_rect.collidepoint(e.pos):
                    self.screen_manager.switch("pause")


    def draw(self, screen):
        screen.fill(colors.BLACK)

        # ---- UI frames ----
        for rect in (
            self.main_btn_rect,
            self.victory_btn_rect,
            self.game_over_btn_rect,
            self.pause_btn_rect,
            self.boss_box_rect,
            self.player_box_rect,
            self.boss_txt_box_rect,
            self.rhythm_box_rect,
        ):
            pygame.draw.rect(screen, colors.WHITE, rect, width=2)

        # ---- Health bars ----
        pygame.draw.rect(screen, colors.HEALTH_BAR_BG, self.player_health_bar_frame_rect)
        pygame.draw.rect(screen, colors.CURRENT_HEALTH, self.player_current_health_rect)
        pygame.draw.rect(screen, colors.WHITE, self.player_health_bar_frame_rect, width=2)


        pygame.draw.rect(screen, colors.HEALTH_BAR_BG, self.boss_health_bar_frame_rect)
        pygame.draw.rect(screen, colors.CURRENT_HEALTH, self.boss_current_health_rect)
        pygame.draw.rect(screen, colors.WHITE, self.boss_health_bar_frame_rect, width=2)


        # ---- Characters ----
        level = self.state.selected_level
        if level in images.boss_images:
            screen.blit(images.boss_images[level][0], (800, 150))
            screen.blit(images.player_images[0], (150, 150))
            screen.blit(
                fonts.LOGO_FONT.render(f"Level {level}", True, colors.WHITE),
                (450, 100),
            )

        # ---- Text ----
        screen.blit(fonts.BUTTON_FONT.render("Pause", True, colors.WHITE),
                    (self.pause_btn_rect.x + 19, self.pause_btn_rect.y + 15))
        screen.blit(fonts.BUTTON_FONT.render("Win", True, colors.WHITE),
                    (self.victory_btn_rect.x + 19, self.victory_btn_rect.y + 15))
        screen.blit(fonts.BUTTON_FONT.render("Lose", True, colors.WHITE),
                    (self.game_over_btn_rect.x + 19, self.game_over_btn_rect.y + 15))
        screen.blit(fonts.BUTTON_FONT.render("Back", True, colors.WHITE),
                    (self.main_btn_rect.x + 19, self.main_btn_rect.y + 15))
        screen.blit(fonts.BUTTON_FONT.render("HarHarHar...", True, colors.WHITE),
                    (self.boss_txt_box_rect.x + 19, self.boss_txt_box_rect.y + 15))
