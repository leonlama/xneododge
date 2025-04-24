import os

# === Screen ===
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "NEODODGE"
VERSION = "v0.3.0"

# === Paths ===
ASSETS_DIR = "assets"
FONT_PATH = os.path.join(ASSETS_DIR, "fonts", "kenney_pixel.ttf")
FONT_NAME = "Kenney Pixel"
TITLE_MUSIC_PATH = os.path.join(ASSETS_DIR, "audio", "title.wav")

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

# === Artifacts ===
ARTIFACT_SCALE = 0.125

# === HUD ===
# Heart display
HEART_SIZE = 2       # Size in pixels for heart icons
HEART_SPACING = 20   # Horizontal spacing between hearts
# Font sizes
HUD_FONT_SIZE_LARGE = 20    # For wave numbers and important info
HUD_FONT_SIZE_MEDIUM = 16   # For secondary information like coin count
HUD_FONT_SIZE_SMALL = 14    # For status effects and timer

# === Scoring ===
TIME_SCORE_RATE = 1.0             # Base points per second survived
WAVE_BONUS_MULTIPLIER = 50        # Points per wave number on completion
COIN_SCORE_VALUE = 10             # Points awarded per coin collected
NEAR_MISS_THRESHOLD = 30          # Pixels for close dodge detection
NEAR_MISS_SCORE = 100             # Points for a successful close dodge
ORB_COMBO_WINDOW = 2.0            # Seconds to chain orb pickups for combo
ORB_COMBO_SCORE = 20              # Points per orb in combo beyond the first