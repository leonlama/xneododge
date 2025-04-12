from src.shop.items.base import BaseShopItem

class OverclockFlask(BaseShopItem):
    def __init__(self):
        super().__init__(
            "Overclock Flask",
            "-30% Artifact Cooldowns for 3 waves",
            price=40,
            rarity="uncommon"
        )

    def apply_effect(self, player, game_view):
        player.status_effects.add("cooldown", duration=30, reduction=0.3)

class EnergySurge(BaseShopItem):
    def __init__(self):
        super().__init__(
            "Energy Surge",
            "+25% Movement Speed for 3 waves",
            price=40,
            rarity="uncommon"
        )

    def apply_effect(self, player, game_view):
        player.status_effects.add("speed", duration=30, magnitude=0.25)

class PointMagnet(BaseShopItem):
    def __init__(self):
        super().__init__(
            "Point Magnet",
            "1.5x Score Multiplier for 3 waves",
            price=50,
            rarity="rare"
        )

    def apply_effect(self, player, game_view):
        player.status_effects.add("multiplier", duration=30, magnitude=1.5)

class ShieldProtocol(BaseShopItem):
    def __init__(self):
        super().__init__(
            "Shield Protocol",
            "Grants a shield that blocks 1 hit",
            price=60,
            rarity="rare"
        )

    def apply_effect(self, player, game_view):
        player.status_effects.add("shield", charges=1)
