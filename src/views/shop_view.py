import arcade
import random
from shop.items.item_registry import ALL_ITEMS

SHOP_FONT = "Kenney Pixel.ttf"

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

        # Draw items
        start_x = self.window.width // 4
        for index, item in enumerate(self.items_for_sale):
            x = start_x + index * 300
            y = self.window.height // 2

            # Item Box
            arcade.draw_rectangle_filled(x, y, 220, 250, arcade.color.BLACK_OLIVE)
            arcade.draw_rectangle_outline(x, y, 220, 250, arcade.color.LIGHT_GREEN, 2)

            # Item Title
            arcade.draw_text(f"{index+1}. {item.name}", x, y + 80,
                             arcade.color.NEON_YELLOW, 18, width=180, align="center", anchor_x="center")

            # Description
            arcade.draw_text(item.description, x, y + 20,
                             arcade.color.WHITE_SMOKE, 12, width=180, align="center", anchor_x="center")

            # Price
            arcade.draw_text(f"{item.cost} 🪙", x, y - 70,
                             arcade.color.GOLD, 16, anchor_x="center")

        # Coin count
        arcade.draw_text(f"Coins: {self.player.coins}", 20, 20, arcade.color.GOLD, 18)

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
                if not item.purchased and self.player.coins >= item.cost:
                    self.player.coins -= item.cost
                    item.purchased = True
                    item.apply_effect(self.player, self.game_view)
                    print(f"✅ Purchased: {item.name}")
