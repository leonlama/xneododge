import arcade
import time
from src.config import PLAYER_SPEED

class StatusEffectManager:
    def __init__(self, player):
        self.player = player
        self.active_effects = {}

    def apply(self, effect_name: str, duration: float = 10.0, magnitude: float = 1.0, charges: int = 0):
        """Apply or refresh a status effect. 'charges' is used for effects like 'shield'."""
        self.active_effects[effect_name] = {
            "time_left": duration,
            "magnitude": magnitude,
            "charges": charges
        }
        self._apply_stat_boost(effect_name, magnitude)

    def _apply_stat_boost(self, effect_name, magnitude):
        if effect_name == "speed":
            self.player.speed_multiplier = 1.0 + 0.5 * magnitude
        elif effect_name == "cooldown":
            self.player.cooldown_multiplier = 1.0 - 0.5 * magnitude
        elif effect_name == "multiplier":
            self.player.score_multiplier = 1.0 + magnitude
        elif effect_name == "shield":
            self.player.shield_active = True
        # Add more if needed

    def update(self, delta_time):
        expired = []
        for name, data in self.active_effects.items():
            if data.get("charges", 0) > 0:
                continue  # shield-like effect, not time-based
            data["time_left"] -= delta_time
            if data["time_left"] <= 0:
                expired.append(name)
        for name in expired:
            del self.active_effects[name]
            self._remove_stat_boost(name)

    def _remove_stat_boost(self, effect_name):
        if effect_name == "speed":
            self.player.speed_multiplier = 1.0
        elif effect_name == "cooldown":
            self.player.cooldown_multiplier = 1.0
        elif effect_name == "multiplier":
            self.player.score_multiplier = 1.0
        elif effect_name == "shield":
            self.player.shield_active = False

    def get_effect_text_lines(self):
        lines = []
        for effect_type, data in self.active_effects.items():
            duration = data["time_left"]
            if effect_type == "speed":
                lines.append(f"Speed +50% ({int(duration)}s)")
            elif effect_type == "multiplier":
                lines.append(f"Score x2 ({int(duration)}s)")
            elif effect_type == "cooldown":
                lines.append(f"Cooldown -50% ({int(duration)}s)")
            elif effect_type == "shield":
                lines.append(f"Shield Active")
        return lines

    def has(self, effect_name):
        return effect_name in self.active_effects

    def get_magnitude(self, effect_name: str) -> float:
        return self.active_effects.get(effect_name, {}).get("magnitude", 0.0)

    def consume_charge(self, effect_name: str) -> bool:
        """Use one charge of a charged effect like 'shield'. Returns True if absorbed, else False."""
        effect = self.active_effects.get(effect_name)
        if effect and effect.get("charges", 0) > 0:
            effect["charges"] -= 1
            if effect["charges"] <= 0:
                del self.active_effects[effect_name]
            return True
        return False
