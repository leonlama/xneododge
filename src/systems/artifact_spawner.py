import arcade
import random
from src.mechanics.artifacts.dash_artifact import DashArtifact

class ArtifactSpawner:
    def __init__(self, artifact_list: arcade.SpriteList):
        self.artifact_list = artifact_list
        self.spawned = False  # Only spawn once for now (or based on waves later)

    def try_spawn_dash(self):
        if not self.spawned:
            x = random.randint(100, 700)
            y = random.randint(100, 500)
            artifact = DashArtifact(x, y)
            self.artifact_list.append(artifact)
            self.spawned = True
