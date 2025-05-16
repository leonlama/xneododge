from src.shop.items.base import BaseShopItem

class OverclockFlask(BaseShopItem):
    def __init__(self):
        super().__init__(
            "Overclock Flask",
            "-30% Artifact Cooldowns for 3 waves",
            price=40,
            rarity="uncommon"
        )

    def apply_effect(self, player, game_view, shop_items=None):
        player.add_temporary_item(self.name, 30)
        player.apply_orb_effect("cooldown")

class EnergySurge(BaseShopItem):
    def __init__(self):
        super().__init__(
            "Energy Surge",
            "+25% Movement Speed for 3 waves",
            price=40,
            rarity="uncommon"
        )

    def apply_effect(self, player, game_view, shop_items=None):
        player.add_temporary_item(self.name, 30)
        player.apply_orb_effect("speed")

class PointMagnet(BaseShopItem):
    def __init__(self):
        super().__init__(
            "Point Magnet",
            "1.5x Score Multiplier for 3 waves",
            price=50,
            rarity="rare"
        )

    def apply_effect(self, player, game_view, shop_items=None):
        player.add_temporary_item(self.name, 30)
        player.apply_orb_effect("multiplier")

class ShieldProtocol(BaseShopItem):
    def __init__(self):
        super().__init__(
            "Shield Protocol",
            "Grants a shield that blocks 1 hit",
            price=60,
            rarity="rare"
        )

    def apply_effect(self, player, game_view, shop_items=None):
        player.add_temporary_item(self.name, 0)  # Duration is not applicable for shield
        player.apply_orb_effect("shield")
