from src.shop.items.base import BaseShopItem

class OverclockFlask(BaseShopItem):
    def __init__(self):
        super().__init__("Overclock Flask", "-30% Artifact Cooldowns (3 waves)", 45, "rare")

    def apply_effect(self, player, game_view):
        player.apply_status_effect("cdr_temp", duration=3, value=0.7)

class EnergySurge(BaseShopItem):
    def __init__(self):
        super().__init__("Energy Surge", "+25% Movement Speed (3 waves)", 45, "rare")

    def apply_effect(self, player, game_view):
        player.apply_status_effect("speed_temp", duration=3, value=1.25)

class PointMagnet(BaseShopItem):
    def __init__(self):
        super().__init__("Point Magnet", "1.5x Score Multiplier (3 waves)", 50, "uncommon")

    def apply_effect(self, player, game_view):
        player.apply_status_effect("score_temp", duration=3, value=1.5)

class ShieldProtocol(BaseShopItem):
    def __init__(self):
        super().__init__("Shield Protocol", "Gain shield that blocks 1 hit", 40, "common")

    def apply_effect(self, player, game_view):
        player.activate_shield()
