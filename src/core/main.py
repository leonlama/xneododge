import arcade
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE
from src.views.start_view import StartView

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = StartView()
    window.show_view(start_view)
    arcade.run()

if __name__ == "__main__":
    main()