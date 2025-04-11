import arcade
import math
from src.config import PLAYER_SCALE, PLAYER_SPRITE_PATH, PLAYER_SPEED
from src.systems.status_effects import StatusEffectManager

class Player(arcade.Sprite):
    DEADZONE_DISTANCE = 2  # adjust this value as needed

    def __init__(self, x, y, window=None):
        super().__init__(PLAYER_SPRITE_PATH, PLAYER_SCALE)
        self.window = window  # 💡 Store window reference here
        self.center_x = x
        self.center_y = y
        self.target_x = x
        self.target_y = y
        self.change_x = 0
        self.change_y = 0
        self.last_dx = 0
        self.last_dy = 0
        self.speed = PLAYER_SPEED
        self.score_multiplier = 1.0
        self.artifact_cooldown_multiplier = 1.0
        self.cooldown_modifier = 1.0  # default = no change
        self.has_shield = False
        self.max_heart_slots = 6  # maximum slots (gray + red hearts)
        self.current_hearts = 3   # start with 3 red hearts
        self.gold_hearts = 0
        self.partial_heart = False
        self.score = 0           # Starting score
        self.coin_count = 0      # Add this in __init__ if not already there
        self.status_effects = StatusEffectManager(self)
        self.invincible = False
        self.invincible_timer = 0
        self.invincible_duration = 1.0  # 1 second
        self.damage_sound = arcade.load_sound("assets/sounds/damage.wav")
        self.extra_heart_slots = 0  # Start with none

    def collect_coin(self, amount: int = 1):
        self.coin_count += amount
        print(f"🪙 Collected coin! Total: {self.coin_count}")

    def update(self, delta_time: float = 1/60):
        self.update_movement(delta_time)
        if self.invincible:
            self.invincible_timer += delta_time
            if int(self.invincible_timer * 10) % 2 == 0:
                self.alpha = 255
            else:
                self.alpha = 100
            if self.invincible_timer >= self.invincible_duration:
                self.invincible = False
                self.alpha = 255

    def update_movement(self, delta_time: float):
        dx = self.target_x - self.center_x
        dy = self.target_y - self.center_y
        distance = math.hypot(dx, dy)

        # Deadzone distance (minimum distance to move)
        DEADZONE = 2

        if distance > DEADZONE:
            move_x = (dx / distance) * self.speed
            move_y = (dy / distance) * self.speed
            self.center_x += move_x * delta_time
            self.center_y += move_y * delta_time
            self.last_dx = dx / distance
            self.last_dy = dy / distance
        else:
            self.center_x = self.target_x
            self.center_y = self.target_y
            self.change_x = 0
            self.change_y = 0

    def set_target(self, x, y):
        self.target_x = x
        self.target_y = y
        # Calculate and store direction as change_x and change_y
        dx = self.target_x - self.center_x
        dy = self.target_y - self.center_y
        distance = math.hypot(dx, dy)
        if distance > 0:
            self.change_x = dx / distance
            self.change_y = dy / distance
        else:
            self.change_x = 0
            self.change_y = 0
       
    def dash(self, distance=150):
        dx, dy = self.last_dx, self.last_dy
        if dx == 0 and dy == 0:
            return  # No direction

        # Dash target
        dash_x = self.center_x + dx * distance
        dash_y = self.center_y + dy * distance

        # Clamp inside screen
        dash_x = max(0, min(dash_x, self.window.width))
        dash_y = max(0, min(dash_y, self.window.height))

        # Set current and target position
        self.center_x = dash_x
        self.center_y = dash_y
        self.target_x = dash_x
        self.target_y = dash_y

        print("Dashing!")
        
    def apply_orb_effect(self, effect_name: str):
        self.status_effects.apply_effect(effect_name)

    def take_damage(self, amount):
        """Apply damage to the player."""
        if self.invincible:
            return  # Skip if invincible

        if "shield" in self.status_effects.active_effects:
            if self.status_effects.active_effects["shield"]["charges"] > 0:
                self.status_effects.active_effects["shield"]["charges"] -= 1
                if self.status_effects.active_effects["shield"]["charges"] <= 0:
                    del self.status_effects.active_effects["shield"]
                print("🛡️ Shield absorbed the hit!")
                return

        # Play damage sound
        arcade.play_sound(self.damage_sound)

        self.invincible = True
        self.invincible_timer = 0
        print(f"⚔️ Player takes {amount} damage!")

        if self.gold_hearts > 0:
            self.gold_hearts -= amount
            if self.gold_hearts < 0:
                remainder = -self.gold_hearts
                self.gold_hearts = 0
                self.current_hearts -= remainder
        else:
            self.current_hearts -= amount

        # Clamp to zero
        self.current_hearts = max(self.current_hearts, 0)

        # Handle partial heart for HUD display
        self.partial_heart = self.current_hearts % 1 != 0

        if self.current_hearts == 0:
            print("💀 Player dead")  # Handle game over here

        # Clamp health
        self.gold_hearts = max(0, self.gold_hearts)

    def add_gray_slot(self):
        if self.extra_heart_slots < 6:
            self.extra_heart_slots += 1
            self.max_heart_slots += 1
            print("🖤 Gray heart slot added!")

    def add_red_heart(self):
        if self.current_hearts < self.max_heart_slots:
            self.current_hearts += 1
            print("❤️ Red heart added!")
        elif self.partial_heart:
            self.partial_heart = False
            self.current_hearts += 1
            print("❤️ Half heart topped up!")

    def add_gold_heart(self):
        self.gold_hearts += 1
        print("💛 Golden heart added!")

    def restore_half_gray(self):
        """Called by Zen Protocol at start of new wave."""
        if self.current_hearts < self.max_heart_slots:
            if self.partial_heart:
                self.current_hearts += 1
                self.partial_heart = False
                print("🖤 Half heart healed to full!")
            else:
                self.partial_heart = True
                print("🖤 Gained 0.5 heart!")
