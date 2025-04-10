import arcade
import time

class StatusEffectManager:
    def __init__(self, player):
        self.player = player
        self.active_effects = {}

    def apply_effect(self, effect_name):
        if effect_name == "speed":
            self.player.speed *= 1.10
            self._add_timed_effect(effect_name, 10, lambda: setattr(self.player, "speed", self.player.speed / 1.10))

        elif effect_name == "multiplier":
            self.player.score_multiplier *= 1.25
            self._add_timed_effect(effect_name, 15, lambda: setattr(self.player, "score_multiplier", self.player.score_multiplier / 1.25))

        elif effect_name == "cooldown":
            self.player.artifact_cooldown_multiplier *= 0.85
            self._add_timed_effect(effect_name, 20, lambda: setattr(self.player, "artifact_cooldown_multiplier", self.player.artifact_cooldown_multiplier / 0.85))

        elif effect_name == "shield":
            self.player.has_shield = True
            # Optional: attach a glowing sprite or visual indicator here
            print("Shield activated!")

    def _add_timed_effect(self, effect_name, duration, on_expire):
        self.active_effects[effect_name] = {
            "expires": time.time() + duration,
            "on_expire": on_expire,
        }

    def update(self):
        current_time = time.time()
        to_remove = []
        for name, effect in self.active_effects.items():
            if current_time > effect["expires"]:
                effect["on_expire"]()
                to_remove.append(name)
        for name in to_remove:
            del self.active_effects[name]
