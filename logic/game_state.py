class GameState:
    BOSS_MAX_HEALTH = {
        1: 200,
        2: 400,
        3: 600,
        4: 800,
        5: 1000,
    }

    def __init__(self):
        self.selected_level = 1
        self.unlocked_until = 1
        self.result = None
        self.player_health = 100
        self.boss_health = 0

    def start_level(self, level):
        self.selected_level = level
        self.boss_health = self.BOSS_MAX_HEALTH[level]

    def player_won(self):
        self.result = "Win"
        if self.selected_level == self.unlocked_until:
            self.unlocked_until += 1

    def player_lost(self):
        self.result = "Lose"
