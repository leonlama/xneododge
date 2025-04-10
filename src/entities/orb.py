import arcade

class Orb(arcade.Sprite):
    def __init__(self, orb_type: str, x: float, y: float, texture: arcade.Texture, scale=0.6):
        super().__init__(texture, scale)
        self.center_x = x
        self.center_y = y
        self.orb_type = orb_type
        
    def apply_effect(self, player):
        """Apply the orb's effect to the player."""
        if self.orb_type == "speed":
            player.status_effects.add("speed", duration=10, magnitude=0.1)
        elif self.orb_type == "multiplier":
            player.status_effects.add("multiplier", duration=10, magnitude=1.5)
        elif self.orb_type == "cooldown":
            player.status_effects.add("cooldown", duration=10, reduction=0.2)
        elif self.orb_type == "shield":
            player.status_effects.add("shield", charges=1)
        elif self.orb_type == "red_heart":
            if player.current_hearts < player.max_hearts:
                player.current_hearts += 1
        elif self.orb_type == "gray_heart":
            player.max_hearts += 1
        elif self.orb_type == "golden_heart":
            player.golden_hearts += 1
