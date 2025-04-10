import arcade
import time

class StatusEffectManager:
    def __init__(self, player):
        self.player = player
        self.active_effects = {}

    def apply_effect(self, effect_name):
        if effect_name == "speed":
            self.player.speed *= 1.10
            self._add_timed_effect(effect_name, 10, lambda: setattr(self.player, "speed", self.player.speed / 1.10), 10)

        elif effect_name == "multiplier":
            self.player.score_multiplier *= 1.25
            self._add_timed_effect(effect_name, 15, lambda: setattr(self.player, "score_multiplier", self.player.score_multiplier / 1.25), 25)

        elif effect_name == "cooldown":
            self.player.artifact_cooldown_multiplier *= 0.85
            self._add_timed_effect(effect_name, 20, lambda: setattr(self.player, "artifact_cooldown_multiplier", self.player.artifact_cooldown_multiplier / 0.85), 15)

        elif effect_name == "shield":
            self.player.has_shield = True
            # Optional: attach a glowing sprite or visual indicator here
            print("Shield activated!")

    def _add_timed_effect(self, effect_name, duration, on_expire, value=0):
        self.active_effects[effect_name] = {
            "expires": time.time() + duration,
            "on_expire": on_expire,
            "time_left": duration,
            "value": value
        }

    def add_effect(self, effect_type: str, duration: float = 10.0):
        """Add an effect to the active effects list with the specified duration."""
        # If the effect is already applied, we'll just update the duration
        if effect_type in self.active_effects:
            self.active_effects[effect_type]["time_left"] = duration
        else:
            # Otherwise, apply the effect
            self.apply_effect(effect_type)

    def update(self, delta_time: float = None):
        if delta_time is None:
            # Maintain backward compatibility with the old time-based approach
            current_time = time.time()
            to_remove = []
            for name, effect in self.active_effects.items():
                if current_time > effect["expires"]:
                    effect["on_expire"]()
                    to_remove.append(name)
                else:
                    # Update time_left for HUD display
                    effect["time_left"] = effect["expires"] - current_time
            for name in to_remove:
                del self.active_effects[name]
        else:
            # New delta_time based approach
            to_remove = []
            for name, effect in self.active_effects.items():
                effect["time_left"] -= delta_time
                if effect["time_left"] <= 0:
                    effect["on_expire"]()
                    to_remove.append(name)
            for name in to_remove:
                del self.active_effects[name]
    
    def get_effect_text_lines(self):
        """Return a list of formatted text lines for each active effect."""
        lines = []
        for effect_type, data in self.active_effects.items():
            if effect_type == "speed":
                lines.append(f"Speed +10% ({int(data['time_left'])}s)")
            elif effect_type == "multiplier":
                lines.append(f"Score x1.25 ({int(data['time_left'])}s)")
            elif effect_type == "cooldown":
                lines.append(f"Cooldown -15% ({int(data['time_left'])}s)")
            elif effect_type == "shield":
                lines.append(f"Shield Active ({int(data['time_left'])}s)")
        return lines
