import os

# === Screen ===
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "NEODODGE"
VERSION = "v0.1.0"

# === Paths ===
ASSETS_DIR = "assets"
FONT_PATH = os.path.join(ASSETS_DIR, "fonts", "kenney_pixel.ttf")
FONT_NAME = "Kenney Pixel"
TITLE_MUSIC_PATH = os.path.join(ASSETS_DIR, "audio", "title.mp3")

# === Player ===
PLAYER_SCALE = 0.035
PLAYER_SPRITE_PATH = os.path.join(ASSETS_DIR, "player", "player.png")
PLAYER_SPEED = 225

# === Orbs ===
ORB_SCALES = {
    "speed": 0.125,
    "multiplier": 0.125,
    "cooldown": 0.125,
    "shield": 0.125,
    "red_heart": 0.035,
    "gray_heart": 0.035,
    "golden_heart": 0.035,
}

# === HUD ===
# Heart display
HEART_SIZE = 2       # Size in pixels for heart icons
HEART_SPACING = 20   # Horizontal spacing between hearts
# Font sizes
HUD_FONT_SIZE_LARGE = 20    # For wave numbers and important info
HUD_FONT_SIZE_MEDIUM = 16   # For secondary information like coin count
HUD_FONT_SIZE_SMALL = 14    # For status effects and timer