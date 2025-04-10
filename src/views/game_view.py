import arcade
from src.entities.player import Player
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT
from src.systems.orb_manager import OrbManager
from src.views.hud import HUD
from src.mechanics.artifacts.artifact_manager import ArtifactManager
from src.systems.artifact_spawner import ArtifactSpawner
from src.systems.coin_spawner import CoinSpawner
from src.systems.coin_manager import CoinManager
from src.systems.enemy_manager import EnemyManager

class DummyWaveManager:
    def __init__(self):
        self.current_wave = 1
        self.time_left = 60
        
class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.player = None
        self.player_list = None
        self.mouse_held = False
        self.orb_manager = OrbManager()
        self.spawn_timer = 0
        self.hud = None
        self.artifact_manager = ArtifactManager()
        self.enemy_manager = None

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, window=self.window)
        self.player_list.append(self.player)
        self.wave_manager = DummyWaveManager()  # Replace with real one later
        self.coin_count = 0  # Start with zero coins
        
        # Initialize enemy manager
        self.enemy_manager = EnemyManager(self.player)

        # Initialize artifact system
        self.artifact_manager = ArtifactManager()
        self.artifact_list = arcade.SpriteList()
        self.artifact_manager.artifact_list = self.artifact_list
        self.artifact_spawner = ArtifactSpawner(self.artifact_list)
        
        # Initialize HUD after artifact_manager is set up
        self.hud = HUD(self.player, self.wave_manager, self.coin_count, self.artifact_manager)

        # Initialize coin system
        self.coin_list = arcade.SpriteList()
        self.coin_spawner = CoinSpawner(self.coin_list)
        self.coin_manager = CoinManager(self.coin_list)

    def on_draw(self):
        self.clear()
        self.player_list.draw()
        self.orb_manager.draw()
        self.artifact_list.draw()
        self.coin_list.draw()
        self.enemy_manager.draw()  # Just before HUD
        self.hud.draw()

    def on_update(self, delta_time: float):
        # Update player (was missing, causing slow/no movement)
        self.player.update()

        self.player_list.update_animation()
        self.orb_manager.update(delta_time)
        self.artifact_manager.update(delta_time)
        self.player.status_effects.update()

        self.spawn_timer += delta_time
        if self.spawn_timer >= 3.0:
            self.orb_manager.spawn_orb()
            self.spawn_timer = 0

        self.orb_manager.check_collisions(self.player, self.apply_effect)
        self.artifact_spawner.try_spawn_dash()
        self.artifact_manager.check_collision(self.player)

        # Update enemy manager
        self.enemy_manager.update(delta_time)
        self.enemy_manager.check_collisions(self.player)

        # Update coin system
        self.coin_list.update_animation()
        self.coin_spawner.update(delta_time)
        self.coin_manager.check_collision(self.player)

    def apply_effect(self, orb_type):
        print(f"Collected orb: {orb_type}")

    def on_mouse_motion(self, x, y, dx, dy):
        if self.mouse_held:
            self.player.set_target(x, y)

    def on_mouse_press(self, x, y, button, modifiers):
        self.mouse_held = True
        self.player.set_target(x, y)

    def on_mouse_release(self, x, y, button, modifiers):
        self.mouse_held = False
        
    def on_key_press(self, key, modifiers):
        if self.artifact_manager.handle_key_press(key, self.player):
            print("Artifact used!")
        # Handle other keys as needed (movement, etc.)