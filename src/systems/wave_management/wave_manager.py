import random

WAVE_TYPES = {
    "Swarm": {"chaser": (4, 6)},
    "Sniper": {"shooter": (2, 4)},
    "Bombardment": {"bomber": (1, 2)},
    "Mixed": {"chaser": (2, 3), "shooter": (1, 2), "wanderer": (1, 2)},
}

class WaveManager:
    def __init__(self):
        self.current_wave = 1
        self.time_left = self._calculate_wave_duration()
        self.wave_types = list(WAVE_TYPES.keys())
        self.has_spawned_this_wave = False
        self.current_wave_type = self.wave_types[0]  # Start with the first wave type
        self.wave_active = True
        self.wave_cooldown = 3.0  # seconds between waves
        self.cooldown_timer = 0
        self._should_start_next_wave = False  # Renamed variable
        self.modifiers = {
            "skip_next_wave": False,
            "reduce_spawn_rate": (1.0, 0),  # (multiplier, remaining waves)
            "ban_chaser": 0,
            "ban_shooter": 0,
            "ban_bomber": 0,
            "ban_wanderer": 0
        }
        assert callable(self.start_next_wave), "start_next_wave has been overwritten!"

    def update(self, delta_time):
        if self.modifiers["skip_next_wave"]:
            self.start_next_wave()
            self.modifiers["skip_next_wave"] = False
            return

        if self.wave_active:
            self.time_left -= delta_time
            if self.time_left <= 0:
                self.wave_active = False
                self.cooldown_timer = self.wave_cooldown
        else:
            self.cooldown_timer -= delta_time
            if self.cooldown_timer <= 0:
                self._should_start_next_wave = True

    def start_next_wave(self):
        self.current_wave += 1
        self._cycle_wave_type()
        self.time_left = self._calculate_wave_duration()
        self.wave_active = True
        self.has_spawned_this_wave = False  # Reset has_spawned_this_wave for the new wave
        self._update_modifiers()
        print(f"[WAVE MANAGER] New wave: {self.current_wave} - {self.current_wave_type}")

    def _cycle_wave_type(self):
        current_index = self.wave_types.index(self.current_wave_type)
        next_index = (current_index + 1) % len(self.wave_types)
        self.current_wave_type = self.wave_types[next_index]

    def consume_wave_trigger(self):
        self._should_start_next_wave = False  # Updated usage

    def get_spawn_recipe(self) -> dict:
        """Return a spawn distribution based on the current wave type."""
        recipe = {}
        for enemy_type, (min_count, max_count) in WAVE_TYPES[self.current_wave_type].items():
            if self.modifiers.get(f"ban_{enemy_type}", 0) > 0:
                continue
            count = random.randint(min_count, max_count)
            count = int(count * self.modifiers["reduce_spawn_rate"][0])
            recipe[enemy_type] = count
        return recipe

    def should_spawn_wave(self):
        if not self.has_spawned_this_wave:
            self.has_spawned_this_wave = True
            return True
        return False

    def _calculate_wave_duration(self):
        return max(2, 5 - self.current_wave * 2) # set wave time return max(10, 30 - self.current_wave * 2)  

    def is_shop_wave(self):
        return self.current_wave % 5 == 0 and self.time_left == 0

    def _update_modifiers(self):
        """Update the wave modifiers, reducing their duration."""
        for key in self.modifiers:
            if isinstance(self.modifiers[key], tuple):
                multiplier, waves_left = self.modifiers[key]
                if waves_left > 0:
                    self.modifiers[key] = (multiplier, waves_left - 1)
            elif self.modifiers[key] > 0:
                self.modifiers[key] -= 1
