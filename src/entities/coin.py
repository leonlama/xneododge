import arcade
import os
from PIL import Image

class Coin(arcade.Sprite):
    """Animated coin that can be collected by the player."""

    def __init__(self, scale=0.5):
        super().__init__(scale=scale)

        # List to hold all animation textures
        self.textures = []
        
        # Animation properties
        self.current_frame = 0
        self.animation_speed = 0.1  # seconds per frame
        self.time_since_last_frame = 0
        
        # Attempt to load the sprite sheet
        try:
            # Path to the sprite sheet
            file_path = "assets/coins/coin_animated.png"
            
            # Open the image with PIL
            sprite_sheet = Image.open(file_path)
            
            # Calculate frame dimensions based on 9 frames
            frame_width = sprite_sheet.width // 9
            frame_height = sprite_sheet.height
            
            # Create frames from the sprite sheet
            for i in range(9):
                # Calculate frame position
                left = i * frame_width
                top = 0
                right = left + frame_width
                bottom = frame_height
                
                # Crop the frame from the sprite sheet
                frame = sprite_sheet.crop((left, top, right, bottom))
                
                # Save the frame to a temporary file
                temp_path = f"temp_coin_frame_{i}.png"
                frame.save(temp_path)
                
                # Load the frame as an arcade texture
                texture = arcade.load_texture(temp_path)
                self.textures.append(texture)
                
                # Remove the temporary file
                os.remove(temp_path)
                
            # Set initial texture
            self.texture = self.textures[0]
            
        except Exception as e:
            print(f"Error loading coin animation: {e}")
            # Fallback to a simple circle if animation fails
            fallback_texture = arcade.make_circle_texture(20, arcade.color.GOLD)
            self.texture = fallback_texture
            # Add the fallback texture to the textures list to avoid division by zero
            self.textures.append(fallback_texture)
    
    def update_animation(self, delta_time: float = 1/60):
        """Update the coin animation."""
        # Skip animation if we don't have textures
        if not self.textures:
            return
            
        self.time_since_last_frame += delta_time
        
        # Change to next frame if it's time
        if self.time_since_last_frame >= self.animation_speed:
            self.current_frame = (self.current_frame + 1) % len(self.textures)
            self.texture = self.textures[self.current_frame]
            self.time_since_last_frame = 0

        # Set properties
        self.scale = 0.85
        self.coin_value = 1