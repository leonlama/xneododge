import arcade
from src.config import FONT_NAME, SCREEN_WIDTH

class HUD:
    def __init__(self, player):
        self.player = player

    def draw(self):
        effects = self.player.status_effects.active_effects
        start_y = 20
        offset = 20

        # Draw each active effect as a text line
        for i, (effect_name, effect_data) in enumerate(effects.items()):
            time_left = round(effect_data["time_left"], 1)
            text = f"{effect_name.capitalize()}: {time_left}s"
            arcade.draw_text(
                text,
                SCREEN_WIDTH - 250,  # Right-align
                start_y + i * offset,
                arcade.color.WHITE,
                14,
                font_name=FONT_NAME
            )
    
    def get_effect_text_lines(self):
        """Returns a list of formatted strings for each active status effect."""
        if not hasattr(self.player.status_effects, 'items'):
            # Handle the case where status_effects is a manager object
            effects = self.player.status_effects.active_effects
            return [f"{effect_name}: {effect_data['time_left']:.1f}s" 
                   for effect_name, effect_data in effects.items()]
        else:
            # Handle the case where status_effects is a dictionary
            return [f"{effect}: {time_left:.1f}s" 
                   for effect, time_left in self.player.status_effects.items()]
