import random

class WaveManager:
    def __init__(self):
        self.current_wave = 1
        self.time_left = self._calculate_wave_duration()  # Use the new method here
        self.wave_type = "Swarm"  # initial type
        self.wave_types = ["Swarm", "Sniper", "Bomber", "Mixed"]
        self.has_spawned_this_wave = False

    def update(self, delta_time):
        self.time_left -= delta_time
        if self.time_left <= 0:
            self.current_wave += 1
            self.time_left = self._calculate_wave_duration()
            self.has_spawned_this_wave = False

    def start_next_wave(self):
        self.current_wave += 1
        self.time_left = self._calculate_wave_duration()  # Use the new method here
        self.wave_type = random.choice(self.wave_types)

    def get_spawn_recipe(self) -> dict:
        """Return a spawn distribution that scales with wave number."""
        min_enemies = 3 + self.current_wave  # e.g. wave 1 = 4, wave 2 = 5...
        max_enemies = 5 + self.current_wave

        total = random.randint(min_enemies, max_enemies)
        types = ["chaser", "wanderer", "shooter", "bomber"]
        result = {t: 0 for t in types}

        for _ in range(total):
            choice = random.choice(types)
            result[choice] += 1

        return result

    def should_spawn_wave(self):
        if not self.has_spawned_this_wave:
            self.has_spawned_this_wave = True
            return True
        return False

    def _calculate_wave_duration(self):
        # You can customize this logic, e.g. longer waves over time
        return max(20, 60 - self.current_wave * 2)
