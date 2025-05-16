class DummyStatusEffects:
    def __init__(self):
        self.effects = {}

    def apply(self, effect_name, **kwargs):
        self.effects[effect_name] = kwargs

    def remove(self, effect_name):
        if effect_name in self.effects:
            del self.effects[effect_name]

    def has(self, name):
        return name in self.effects

class DummyPlayer:
    def __init__(self, current_hearts=3, max_hearts=3, golden_hearts=0, max_heart_slots=3):
        self.current_hearts = current_hearts
        self.max_hearts = max_hearts
        self.golden_hearts = golden_hearts
        self.max_heart_slots = max_heart_slots
        self.permanent_items = []
        self.temporary_items = []
        self.status_effects = DummyStatusEffects()
        self.permanent_cooldown_reduction = 0.0
        self.has_second_chance = False
        self.orb_spawn_boost = 0.0
        self.coin_drop_boost = 0.0
        self.absorption_chance = 0.0
        self.permanent_effects = {
            "cooldown_reduction": 0.0,
            "movement_speed": 0.0,
            "orb_spawn_chance": 0.0,
            "coin_drop_chance": 0.0,
            "absorb_chance": 0.0
        }

    def heal(self, amount):
        self.current_hearts = min(self.current_hearts + amount, self.max_heart_slots)

    def add_golden_heart(self):
        self.golden_hearts += 1

    def add_max_heart(self):
        self.max_hearts += 1
        self.max_heart_slots += 1

    def add_temporary_item(self, name, duration):
        self.temporary_items.append({"name": name, "duration": duration})

    def add_permanent_item(self, name):
        self.permanent_items.append({"name": name})

    def apply_orb_effect(self, effect_name):
        self.status_effects.apply(effect_name)

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

    def skip_wave(self):
        self.modifiers["skip_next_wave"] = True


class DummyGameView:
    def __init__(self):
        self.wave_manager = DummyWaveManager()
        self.shop_view = None
        self.score = 0

    def add_score(self, amount):
        self.score += amount
