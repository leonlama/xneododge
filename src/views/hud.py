import arcade
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT, FONT_NAME, HEART_SIZE, HEART_SPACING, HUD_FONT_SIZE_LARGE, HUD_FONT_SIZE_MEDIUM, HUD_FONT_SIZE_SMALL

class HUD:
    def __init__(self, player, wave_manager, coin_count, artifact_manager):
        self.player = player
        self.wave_manager = wave_manager
        self.coin_count = coin_count
        self.artifact_manager = artifact_manager
        self.heart_images = {
            'red': "assets/hud/hearts/heart.png",
            'gray': "assets/hud/hearts/heart_empty.png",
            'gold': "assets/hud/hearts/heart_gold.png",
            'half': "assets/hud/hearts/heart_half.png"
        }
        self.coin_texture = arcade.load_texture("assets/coins/bank.png")

    def draw_centered_texture(self, center_x, center_y, size, texture_path):
        sprite = arcade.Sprite(texture_path, scale=size / 64)
        sprite.center_x = center_x
        sprite.center_y = center_y

        # Add to a temporary SpriteList and draw it
        temp_list = arcade.SpriteList()
        temp_list.append(sprite)
        temp_list.draw()

    def draw_coin_counter(self):
        icon_x = SCREEN_WIDTH - 80
        icon_y = 30

        # Draw coin icon using a sprite with scaled down size
        coin_sprite = arcade.Sprite(self.coin_texture, scale=0.035)
        coin_sprite.center_x = icon_x
        coin_sprite.center_y = icon_y

        # Add to a temporary SpriteList and draw it
        temp_list = arcade.SpriteList()
        temp_list.append(coin_sprite)
        temp_list.draw()

        # Draw coin count
        arcade.draw_text(f"{self.player.coin_count}", icon_x + 40, icon_y - 8,
                         arcade.color.GOLD, 18, font_name=FONT_NAME)

    def draw(self):
        # Top center: Wave and time left
        arcade.draw_text(
            f"Wave {self.wave_manager.current_wave}: {self.wave_manager.current_wave_type}",
            SCREEN_WIDTH // 2, SCREEN_HEIGHT - 30,
            arcade.color.LIME_GREEN, 20, anchor_x="center", font_name=FONT_NAME
        )
        arcade.draw_text(
            f"{int(self.wave_manager.time_left)}s left",
            SCREEN_WIDTH // 2, SCREEN_HEIGHT - 55,
            arcade.color.LIGHT_GREEN, 14, anchor_x="center", font_name=FONT_NAME
        )

        # Top left: Hearts and score
        y_offset = SCREEN_HEIGHT - 30
        x_offset = 30

        # Draw red hearts (filled HP)
        for i in range(int(self.player.current_hearts)):
            self.draw_centered_texture(x_offset, y_offset, HEART_SIZE, self.heart_images['red'])
            x_offset += HEART_SPACING

        # Draw half heart if needed
        if self.player.partial_heart:
            self.draw_centered_texture(x_offset, y_offset, HEART_SIZE, self.heart_images['half'])
            x_offset += HEART_SPACING

        # Draw gray heart slots ONLY IF player has extra
        extra_heart_slots = self.player.max_heart_slots - int(self.player.current_hearts) - (1 if self.player.partial_heart else 0)
        for _ in range(extra_heart_slots):
            self.draw_centered_texture(x_offset, y_offset, HEART_SIZE, self.heart_images['gray'])
            x_offset += HEART_SPACING

        # Draw golden hearts stacked next to red/gray
        for i in range(self.player.gold_hearts):
            self.draw_centered_texture(x_offset, y_offset, HEART_SIZE, self.heart_images['gold'])
            x_offset += HEART_SPACING

        arcade.draw_text(f"Score: {self.player.score}", 10, y_offset - 35,
                         arcade.color.WHITE, HUD_FONT_SIZE_SMALL, font_name=FONT_NAME)

        # Top right: Active effects
        effects = self.player.status_effects.get_effect_text_lines()
        for i, line in enumerate(effects):
            arcade.draw_text(line, SCREEN_WIDTH - 10, SCREEN_HEIGHT - 30 - i * 20,
                             arcade.color.WHITE, HUD_FONT_SIZE_SMALL, anchor_x="right", font_name=FONT_NAME)

        # Bottom right: Coins
        self.draw_coin_counter()
        
        # Bottom left: Artifact status
        if "dash" in self.artifact_manager.active_artifacts:
            cooldown = self.artifact_manager.cooldowns.get("dash", 0)
            status = "READY" if cooldown <= 0 else f"CD: {cooldown:.1f}s"
            arcade.draw_text(f"Dash: {status}", 10, 10, arcade.color.CYAN, 14, font_name=FONT_NAME)
