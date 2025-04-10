import arcade
from src.entities.player import Player
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT
from src.systems.orb_manager import OrbManager

class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.player = None
        self.player_list = None
        self.mouse_held = False
        self.orb_manager = OrbManager()
        self.spawn_timer = 0

    def setup(self):
        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player)

    def on_draw(self):
        self.clear()
        self.player_list.draw()
        self.orb_manager.draw()

    def on_update(self, delta_time: float):
        self.player.update_movement(delta_time)
        self.player_list.update()
        self.player_list.update_animation()
        
        # Update orb manager
        self.orb_manager.update(delta_time)
        
        # Update player status effects
        self.player.status_effects.update()
        
        # Spawn orbs every few seconds
        self.spawn_timer += delta_time
        if self.spawn_timer >= 3.0:  # Spawn every 3 seconds
            self.orb_manager.spawn_orb()
            self.spawn_timer = 0
            
        # Check for collisions
        self.orb_manager.check_collisions(self.player, self.apply_effect)

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