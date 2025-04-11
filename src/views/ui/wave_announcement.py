import arcade

class WaveAnnouncement:
    def __init__(self, duration: float = 2.5):
        self.message = ""
        self.total_duration = duration
        self.timer = 0
        self.visible = False
        self.fade_delay = 1.0  # Increased delay before fade starts

    def show_wave(self, wave_number, wave_type):
        self.message = f"Wave {wave_number}: {wave_type}"
        self.timer = 0
        self.visible = True

    def update(self, delta_time: float):
        if self.visible:
            self.timer += delta_time
            if self.timer > self.total_duration:
                self.visible = False

    def draw(self, screen_width, screen_height):
        if not self.visible:
            return

        x = screen_width // 2
        y = screen_height // 2 + 50
        fade_alpha = 255

        if self.timer > self.fade_delay:
            fade_alpha = int(255 * (1 - (self.timer - self.fade_delay) / (self.total_duration - self.fade_delay)))
            fade_alpha = max(0, min(255, fade_alpha))

        text = arcade.Text(
            self.message,
            x, y,
            arcade.color.YELLOW,
            font_size=28,
            anchor_x="center",
            anchor_y="center",
            font_name="Kenney Pixel",
            bold=True
        )
        text.alpha = fade_alpha
        text.draw()
