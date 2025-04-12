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
            reduction = kwargs.get("reduction", 0.2)  # Default 20% faster
            duration = kwargs.get("duration", 10)
            self.active_effects["cooldown"] = {
                "reduction": reduction,
                "time_left": duration
            }
            self.player.cooldown_modifier = 1.0 - reduction

        elif effect_type == "shield":
            self.player.has_shield = True
            self.active_effects["shield"] = {"charges": kwargs["charges"]}
            print("Shield activated!")
            
        elif effect_type == "ghost_dash":
            duration = kwargs.get("duration", 1.5)
            self.active_effects["ghost_dash"] = {
                "duration": duration,
                "active": False  # Will be set to True when dash is used
            }
            print("Ghost Dash ready!")
            
        elif effect_type == "second_chance":
            self.active_effects["second_chance"] = {
                "used": False
            }
            print("Second Chance active!")
            
        elif effect_type == "artifact_insurance":
            self.active_effects["artifact_insurance"] = {
                "used": False
            }
            print("Artifact Insurance active!")

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
                self.player.cooldown_modifier = 1.0  # reset cooldown modifier
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
                lines.append(f"Cooldown -{int(data.get('reduction', 0) * 100)}% ({int(data.get('time_left', 0))}s)")
            elif effect_type == "shield":
                lines.append(f"Shield Active ({data.get('charges', 1)} charges)")
            elif effect_type == "ghost_dash":
                lines.append(f"Ghost Dash Ready")
            elif effect_type == "second_chance":
                lines.append(f"Second Chance Active")
            elif effect_type == "artifact_insurance":
                lines.append(f"Artifact Insurance Active")
        return lines
