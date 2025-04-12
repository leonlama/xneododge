from src.shop.items.base import BaseShopItem

class SkipTicket(BaseShopItem):
    def __init__(self):
        super().__init__("Skip Ticket", "Skip the next wave and earn bonus score.", 35, rarity="common")
        
    def apply_effect(self, player, game_view):
        game_view.wave_manager.modifiers["skip_next_wave"] = True
        game_view.add_score(200)

class Smokescreen(BaseShopItem):
    def __init__(self):
        super().__init__("Smokescreen", "-25% enemies for next 5 waves.", 40, rarity="common")

    def apply_effect(self, player, game_view):
        game_view.wave_manager.modifiers["reduce_spawn_rate"] = (0.75, 5)

class ChaserRepellent(BaseShopItem):
    def __init__(self):
        super().__init__("Chaser Repellent", "No Chasers for next 5 waves.", 40, rarity="common")

    def apply_effect(self, player, game_view):
        game_view.wave_manager.modifiers["ban_chaser"] = 5

class EMPPulse(BaseShopItem):
    def __init__(self):
        super().__init__("EMP Pulse", "No Shooters for next 5 waves.", 45, rarity="uncommon")      

    def apply_effect(self, player, game_view):
        game_view.wave_manager.modifiers["ban_shooter"] = 5

class BombDefuser(BaseShopItem):
    def __init__(self):
        super().__init__("Bomb Defuser", "No Bombers for next 5 waves.", 45, rarity="uncommon")

    def apply_effect(self, player, game_view):
        game_view.wave_manager.modifiers["ban_bomber"] = 5

class MazeJammer(BaseShopItem):
    def __init__(self):
        super().__init__("Maze Jammer", "No Wanderers for next 5 waves.", 45, rarity="uncommon")

    def apply_effect(self, player, game_view):
        game_view.wave_manager.modifiers["ban_wanderer"] = 5
        player.status_effects.add("shield", charges=1)
