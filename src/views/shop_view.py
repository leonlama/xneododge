import arcade
import random
from src.shop.items.item_registry import ALL_ITEMS

SHOP_FONT = "Kenney Pixel.ttf"
BANNER_FONT = "Kenney Future"

class ShopView(arcade.View):
    def __init__(self, player, game_view):
        super().__init__()
        self.player = player
        self.game_view = game_view
        self.items_for_sale = random.sample(ALL_ITEMS, 3)
        self.background_color = arcade.color.DARK_SLATE_BLUE

    def on_show(self):
        arcade.set_background_color(self.background_color)

    def on_draw(self):
        self.clear()

        # Draw glowing shop title
        arcade.draw_text("🛒 NEO SHOP", self.window.width // 2, self.window.height - 80,
                         arcade.color.YELLOW, 40, anchor_x="center", font_name=SHOP_FONT)

        # Draw shop banner
        arcade.draw_text(
            "🛒 CHOOSE YOUR BLESSING",
            self.window.width // 2,
            self.window.height - 120,
            arcade.color.YELLOW_ORANGE,
            28,
            anchor_x="center",
            font_name=BANNER_FONT
        )

        # Draw items
        start_x = self.window.width // 4
        for index, item in enumerate(self.items_for_sale):
            x = start_x + index * 300
            y = self.window.height // 2

            # Item Box
            half_width = 110
            half_height = 125
            arcade.draw_lrbt_rectangle_filled(
                x - half_width, x + half_width,
                y - half_height, y + half_height,
                arcade.color.BLACK_OLIVE
            )

            # Replacement for draw_rectangle_outline
            half_width_outline = 220 // 2
            half_height_outline = 250 // 2

            left = x - half_width_outline
            right = x + half_width_outline
            top = y + half_height_outline
            bottom = y - half_height_outline

            line_thickness = 2
            arcade.draw_line(left, top, right, top, arcade.color.LIGHT_GREEN, line_thickness)
            arcade.draw_line(right, top, right, bottom, arcade.color.LIGHT_GREEN, line_thickness)
            arcade.draw_line(right, bottom, left, bottom, arcade.color.LIGHT_GREEN, line_thickness)
            arcade.draw_line(left, bottom, left, top, arcade.color.LIGHT_GREEN, line_thickness)

            # Item Title
            arcade.draw_text(f"{index+1}. {item.name}", x, y + 80,
                             arcade.color.GOLD, 18, width=180, align="center", anchor_x="center")

            # Description
            arcade.draw_text(item.description, x, y + 20,
                             arcade.color.WHITE_SMOKE, 12, width=180, align="center", anchor_x="center")

            # Price
            arcade.draw_text(f"{item.cost} 🪙", x, y - 70,
                             arcade.color.GOLD, 16, anchor_x="center")

        # Coin count
        arcade.draw_text(f"Coins: {self.player.coin_count}", 20, 20, arcade.color.GOLD, 18)

        # Hint
        arcade.draw_text("Press [1] [2] [3] to buy, [Esc] to skip",
                         self.window.width // 2, 40, arcade.color.GRAY, 14, anchor_x="center")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            self.window.show_view(self.game_view)
            return

        index_map = {
            arcade.key.KEY_1: 0,
            arcade.key.KEY_2: 1,
            arcade.key.KEY_3: 2
        }

        if key in index_map:
            index = index_map[key]
            if index < len(self.items_for_sale):
                item = self.items_for_sale[index]
                if not item.purchased and self.player.coin_count >= item.cost:
                    self.player.coin_count -= item.cost
                    item.purchased = True
                    item.apply_effect(self.player, self.game_view)
                    print(f"✅ Purchased: {item.name}")
