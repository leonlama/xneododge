class DummyStatusEffects:
    def __init__(self):
        self.effects = {}

    def add(self, name, **kwargs):
        self.effects[name] = kwargs

    def has(self, name):
        return name in self.effects

class DummyPlayer:
    def __init__(self, current_hearts=3, max_hearts=3, golden_hearts=0):
        self.current_hearts = current_hearts
        self.max_hearts = max_hearts
        self.golden_hearts = golden_hearts
        self.max_gray_hearts = 0
        self.status_effects = DummyStatusEffects()
        self.permanent_cooldown_reduction = 0.0
        self.has_second_chance = False
        self.orb_spawn_boost = 0.0
        self.coin_drop_boost = 0.0
        self.absorption_chance = 0.0
    
    def heal(self, amount):
        self.current_hearts = min(self.max_hearts, self.current_hearts + amount)
    
    def add_golden_heart(self):
        self.golden_hearts += 1

class DummyWaveManager:
    def __init__(self):
        self.modifiers = {
            "skip_next_wave": False,
            "reduce_spawn_rate": (1.0, 0),
            "ban_chaser": 0,
            "ban_shooter": 0,
            "ban_bomber": 0,
            "ban_wanderer": 0
        }

class DummyGameView:
    def __init__(self):
        self.wave_manager = DummyWaveManager()
        self.shop_view = None
        self.score = 0

    def add_score(self, amount):
        self.score += amount
