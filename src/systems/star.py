import arcade
import random

STAR_COLORS = [
    arcade.color.WHITE, arcade.color.LIGHT_GRAY, arcade.color.LIGHT_YELLOW,
    arcade.color.LIGHT_BLUE, arcade.color.LIGHT_PINK, arcade.color.LIGHT_GREEN,
    arcade.color.PURPLE, arcade.color.BABY_BLUE
]

STAR_COUNT = 80
STAR_SPEED_RANGE = (20, 100)
STAR_SIZE_RANGE = (1, 3)

class Star:
    def __init__(self, x, y, dx, dy, radius, color):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.radius = radius
        self.color = color

    def update(self, delta_time: float):
        self.x += self.dx * delta_time
        self.y += self.dy * delta_time

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.radius, self.color)

class StarManager:
    def __init__(self):
        self.stars = []
        self.reset()

    def reset(self):
        from src.config import SCREEN_WIDTH, SCREEN_HEIGHT
        self.stars.clear()
        for _ in range(STAR_COUNT):
            x = random.uniform(0, SCREEN_WIDTH)
            y = random.uniform(0, SCREEN_HEIGHT)
            dx = random.uniform(-15, 15)
            dy = -random.uniform(*STAR_SPEED_RANGE)
            radius = random.uniform(*STAR_SIZE_RANGE)
            color = random.choice(STAR_COLORS)
            self.stars.append(Star(x, y, dx, dy, radius, color))

    def update(self, delta_time: float):
        from src.config import SCREEN_WIDTH, SCREEN_HEIGHT
        for star in self.stars:
            star.update(delta_time)
            if star.y < 0 or star.x < 0 or star.x > SCREEN_WIDTH:
                star.x = random.uniform(0, SCREEN_WIDTH)
                star.y = SCREEN_HEIGHT + 10
                star.dy = -random.uniform(*STAR_SPEED_RANGE)
                star.dx = random.uniform(-15, 15)

    def draw(self):
        for star in self.stars:
            star.draw()
