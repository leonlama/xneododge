import arcade

class Orb(arcade.Sprite):
    def __init__(self, orb_type: str, x: float, y: float, texture: arcade.Texture, scale=0.6):
        super().__init__(texture, scale)
        self.center_x = x
        self.center_y = y
        self.orb_type = orb_type
        
    def apply_effect(self, player):
        """Apply the orb's effect to the player."""
        orb_type = self.orb_type
        if orb_type in ["speed", "multiplier", "cooldown"]:
            player.status_effects.add_effect(orb_type, 10)
        elif orb_type == "shield":
            print("Shield activated!")
            player.status_effects.add_effect("shield", 10)
        elif orb_type == "red_heart":
            if player.current_hearts < player.max_hearts:
                player.current_hearts += 1
        elif orb_type == "gray_heart":
            player.max_hearts += 1
        elif orb_type == "golden_heart":
            player.golden_hearts += 1
