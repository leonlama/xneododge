from src.shop.items.base import BaseShopItem

class HeartSnack(BaseShopItem):
    def __init__(self):
        super().__init__(
            name="Heart Snack",
            description="+1 Red Heart (heals if not full)",
            cost=20
        )

    def apply_effect(self, player, game_view):
        player.heal(1)

class EmptyShell(BaseShopItem):
    def __init__(self):
        super().__init__(
            name="Empty Shell",
            description="+1 Gray Heart Slot",
            cost=25
        )

    def apply_effect(self, player, game_view):
        player.max_hearts += 1  # Allows more hearts to be healed into

class GoldenKernel(BaseShopItem):
    def __init__(self):
        super().__init__(
            name="Golden Kernel",
            description="+1 Golden Heart (overheal)",
            cost=40
        )

    def apply_effect(self, player, game_view):
        player.gold_hearts += 1
