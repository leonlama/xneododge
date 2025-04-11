import arcade

class ArtifactManager:
    def __init__(self):
        self.active_artifacts = {}
        self.cooldowns = {}
        self.max_cooldowns = {"dash": 5.0}  # 5s base cooldown
        self.artifact_list = None
        self.artifact_collect_sound = arcade.load_sound("assets/sounds/artifact_collect.mp3")

    def collect(self, artifact_type):
        self.active_artifacts[artifact_type] = True
        self.cooldowns[artifact_type] = 0  # Ready to use

    def handle_key_press(self, key, player):
        for artifact_type, active in self.active_artifacts.items():
            if active:
                if artifact_type == "dash" and key == arcade.key.SPACE:
                    if self.cooldowns.get(artifact_type, 0) <= 0:
                        self._use_dash(player)
                        self.cooldowns[artifact_type] = self.max_cooldowns[artifact_type] * player.cooldown_modifier
                        return True
        return False

    def update(self, delta_time):
        for key in self.cooldowns:
            if self.cooldowns[key] > 0:
                self.cooldowns[key] -= delta_time

    def _use_dash(self, player):
        dx, dy = player.change_x, player.change_y
        if dx == dy == 0:
            return
        magnitude = (dx ** 2 + dy ** 2) ** 0.5
        player.center_x += (dx / magnitude) * 80
        player.center_y += (dy / magnitude) * 80
        print("Dashed!")
        
    def check_collision(self, player):
        hit_list = arcade.check_for_collision_with_list(player, self.artifact_list)
        for artifact in hit_list:
            name = artifact.artifact_type  # Using artifact_type from DashArtifact
            self.active_artifacts[name] = True
            self.cooldowns[name] = 0
            print(f"Collected artifact: {name}")
            arcade.play_sound(self.artifact_collect_sound)
            artifact.remove_from_sprite_lists()
