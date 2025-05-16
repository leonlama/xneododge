from src.shop.items.base import BaseShopItem

class HeartSnack(BaseShopItem):
    def __init__(self):
        super().__init__("Heart Snack", "Restore 1 red heart.", 25, rarity="common")

    def apply_effect(self, player, game_view, shop_items=None):
        player.heal(1)
        player.add_temporary_item(self.name, duration=None)


class EmptyShell(BaseShopItem):
    def __init__(self):
        super().__init__("Empty Shell", "Gain 1 max gray heart slot.", 30, rarity="common")

    def apply_effect(self, player, game_view, shop_items=None):
        player.max_heart_slots += 1
        player.add_permanent_item(self.name)


class GoldenKernel(BaseShopItem):
    def __init__(self):
        super().__init__("Golden Kernel", "Gain 1 golden heart (overheal).", 40, rarity="uncommon")

    def apply_effect(self, player, game_view, shop_items=None):
        player.add_golden_heart()
        player.add_temporary_item(self.name, duration=None)
