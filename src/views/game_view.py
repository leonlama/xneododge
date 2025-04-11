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
from src.systems.wave_management.wave_manager import WaveManager
from src.views.ui.wave_announcement import WaveAnnouncement
from src.views.shop_view import ShopView 

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
        self.wave_announcement = None
        self.took_damage_this_wave = False  # Track if player took damage this wave
        self.shop_triggered = False  # Track if shop has been triggered

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, window=self.window)
        self.player_list.append(self.player)
        self.wave_manager = WaveManager()  # Use the real wave manager
        #self.coins = 0  # Start with zero coins
        
        # Initialize enemy manager
        self.enemy_manager = EnemyManager(self.player)

        # Initialize artifact system
        self.artifact_manager = ArtifactManager()
        self.artifact_list = arcade.SpriteList()
        self.artifact_manager.artifact_list = self.artifact_list
        self.artifact_spawner = ArtifactSpawner(self.artifact_list)
        
        # Initialize HUD after artifact_manager is set up
        self.hud = HUD(self.player, self.wave_manager, self.artifact_manager)

        # Initialize coin system
        self.coin_list = arcade.SpriteList()
        self.coin_spawner = CoinSpawner(self.coin_list)
        self.coin_manager = CoinManager(self.player, self.coin_list)

        # Initialize wave announcement
        self.wave_announcement = WaveAnnouncement()

    def on_draw(self):
        self.clear()
        self.player_list.draw()
        self.orb_manager.draw()
        self.artifact_list.draw()
        self.coin_list.draw()
        self.enemy_manager.draw()  # Just before HUD
        self.enemy_manager.bullet_list.draw()  # Draw enemy bullets
        self.hud.draw()
        if self.wave_announcement:
            self.wave_announcement.draw(SCREEN_WIDTH, SCREEN_HEIGHT)

    def on_update(self, delta_time: float):
        # Update player (was missing, causing slow/no movement)
        self.player.update()

        # Update wave manager
        self.wave_manager.update(delta_time)

        if self.wave_manager._should_start_next_wave:
            if not self.took_damage_this_wave:
                self.player.restore_half_gray()
            self.took_damage_this_wave = False  # Reset for the next wave
            
            # Check for shop wave AFTER wave ends
            if self.wave_manager.current_wave % 5 == 0 and not self.shop_triggered:
                print("🛒 Entering shop view...")
                shop_view = ShopView(self.player, self.coin_manager, self.return_from_shop)
                self.window.show_view(shop_view)
                self.shop_triggered = True
                return  # Pause start_next_wave() until the shop is done

            self.wave_manager.start_next_wave()
            self.wave_announcement.show_wave(self.wave_manager.current_wave, self.wave_manager.current_wave_type)
            distribution = self.wave_manager.get_spawn_recipe()
            self.enemy_manager.spawn_wave(distribution)
            self.wave_manager.consume_wave_trigger()

            # Reset shop_triggered after starting a new wave
            if self.wave_manager.current_wave % 5 != 0:
                self.shop_triggered = False

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

        # Update enemy bullets and check for collision
        self.enemy_manager.bullet_list.update()
        self.enemy_manager.check_bullet_collisions(self.player)

        # Spawn enemies based on wave manager's recipe if not already spawned this wave
        if self.wave_manager.should_spawn_wave():
            self.enemy_manager.trim_enemies_for_new_wave()
            distribution = self.wave_manager.get_spawn_recipe()
            self.enemy_manager.spawn_wave(distribution)
            self.wave_announcement.show_wave(self.wave_manager.current_wave, self.wave_manager.current_wave_type)

        if self.wave_announcement:
            self.wave_announcement.update(delta_time)

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

    def return_from_shop(self):
        self.setup_wave_after_shop = True  # Optional flag if needed
        self.window.show_view(self)