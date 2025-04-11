class BaseShopItem:
    def __init__(self, name, description, cost=5, rarity="common"):
        self.name = name
        self.description = description
        self.cost = cost
        self.rarity = rarity

    def apply(self, player):
        self.apply_effect(player)

    def apply_effect(self, player, game_view):
        """Override this in child classes to apply effect to the player or game."""
        raise NotImplementedError("Each shop item must implement apply_effect()")

    def is_available(self, player, game_view):
        """Optional: You can override to make items conditional."""
        return True
