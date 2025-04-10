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