import arcade
import time
from src.config import PLAYER_SPEED

class StatusEffectManager:
    def __init__(self, player):
        self.player = player
        self.active_effects = {}

    def add(self, effect_type, **kwargs):
        if effect_type == "speed":
            self.player.speed *= (1 + kwargs["magnitude"])
            self._add_timed_effect(effect_type, kwargs["duration"], lambda: setattr(self.player, "speed", self.player.speed / (1 + kwargs["magnitude"])))

        elif effect_type == "multiplier":
            self.player.score_multiplier *= kwargs["magnitude"]
            self._add_timed_effect(effect_type, kwargs["duration"], lambda: setattr(self.player, "score_multiplier", self.player.score_multiplier / kwargs["magnitude"]))

        elif effect_type == "cooldown":
            self.player.artifact_cooldown_multiplier *= (1 - kwargs["reduction"])
            self._add_timed_effect(effect_type, kwargs["duration"], lambda: setattr(self.player, "artifact_cooldown_multiplier", self.player.artifact_cooldown_multiplier / (1 - kwargs["reduction"])))

        elif effect_type == "shield":
            self.player.has_shield = True
            self.active_effects["shield"] = {"charges": kwargs["charges"]}
            print("Shield activated!")

    def _add_timed_effect(self, effect_name, duration, on_expire):
        self.active_effects[effect_name] = {
            "time": duration,
            "on_expire": on_expire
        }

    def update(self):
        expired_keys = []
        for effect, data in self.active_effects.items():
            if "time" in data:
                data["time"] -= 1 / 60  # assuming 60 FPS
                if data["time"] <= 0:
                    expired_keys.append(effect)

        for effect in expired_keys:
            print(f"[STATUS] {effect} expired.")
            if effect == "speed":
                self.player.speed = PLAYER_SPEED  # reset speed to base speed
            elif effect == "multiplier":
                self.player.score_multiplier = 1.0  # reset score multiplier
            elif effect == "cooldown":
                self.player.artifact_cooldown_multiplier = 1.0  # reset cooldown multiplier
            elif effect == "shield":
                self.player.has_shield = False  # deactivate shield
            del self.active_effects[effect]
    
    def get_effect_text_lines(self):
        lines = []
        for effect_type, data in self.active_effects.items():
            if effect_type == "speed":
                lines.append(f"Speed +{int(data.get('magnitude', 0) * 100)}% ({int(data.get('time', 0))}s)")
            elif effect_type == "multiplier":
                lines.append(f"Score x{data.get('magnitude', 1)} ({int(data.get('time', 0))}s)")
            elif effect_type == "cooldown":
                lines.append(f"Cooldown -{int(data.get('reduction', 0) * 100)}% ({int(data.get('time', 0))}s)")
            elif effect_type == "shield":
                lines.append(f"Shield Active ({data.get('charges', 1)} charges)")
        return lines
