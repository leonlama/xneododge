class BaseShopItem:
    def __init__(self, name, description, cost, icon_path=None):
        self.name = name
        self.description = description
        self.cost = cost
        self.icon_path = icon_path  # Optional: could be used in the shop view
        self.purchased = False

    def apply_effect(self, player, game_view):
        """Override this in child classes to apply effect to the player or game."""
        raise NotImplementedError("Each shop item must implement apply_effect()")

    def is_available(self, player, game_view):
        """Optional: You can override to make items conditional."""
        return True
