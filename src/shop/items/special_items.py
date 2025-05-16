from src.shop.items.base import BaseShopItem
import random

class ShopResetChip(BaseShopItem):
    def __init__(self):
        super().__init__("Shop Reset Chip", "Refresh shop items instantly", 40, "uncommon")

    def apply_effect(self, player, game_view, shop_items=None):
        player.add_permanent_item(self.name)
        if hasattr(game_view, 'shop_view'):
            game_view.shop_view.refresh_items()
        else:
            print("[⚠️] No shop view found to refresh.")


class LuckyDraw(BaseShopItem):
    def __init__(self):
        super().__init__("Lucky Draw", "Get 1 random item for free", 60, "uncommon")

    def apply_effect(self, player, game_view, shop_items=None):
        if not shop_items:
            print("[⚠️] No shop items available for Lucky Draw.")
            return

        random_item = random.choice(shop_items)
        print(f"[🎁] Lucky Draw selected: {random_item.name}")
        random_item.apply_effect(player, game_view, shop_items)

        # Optional: mark it as temporary UI highlight (won’t reapply logic)
        player.add_temporary_item(random_item.name, duration=None)


class MysteryBox(BaseShopItem):
    def __init__(self):
        super().__init__("Mystery Box", "50% chance: +2 golden hearts, else nothing", 75, "rare")

    def apply_effect(self, player, game_view, shop_items=None):
        player.add_permanent_item(self.name)
        if random.random() < 0.5:
            player.gold_hearts += 2
            print("🌟 Mystery Box success: +2 golden hearts!")
        else:
            if hasattr(game_view, "display_popup"):
                game_view.display_popup("Mystery Box was empty!")
            print("🕳️ Mystery Box failed: no reward.")
