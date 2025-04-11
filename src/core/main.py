import arcade
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE
from src.views.start_view import StartView
from src.views.tests.test_health_items import HealthItemTestView
import sys

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    if len(sys.argv) > 1 and sys.argv[1] == "test_health":
        window.show_view(HealthItemTestView())
    else:
        start_view = StartView()
        window.show_view(start_view)
    arcade.run()

if __name__ == "__main__":
    main()