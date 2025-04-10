import arcade

class Player(arcade.Sprite):
    def __init__(self, x, y, scale=0.5):
        texture_path = "assets/player/player.png"
        super().__init__(texture_path, scale)
        self.center_x = x
        self.center_y = y
        self.speed = 5

    def update_movement(self, keys):
        if keys[arcade.key.W] or keys[arcade.key.UP]:
            self.center_y += self.speed
        if keys[arcade.key.S] or keys[arcade.key.DOWN]:
            self.center_y -= self.speed
        if keys[arcade.key.A] or keys[arcade.key.LEFT]:
            self.center_x -= self.speed
        if keys[arcade.key.D] or keys[arcade.key.RIGHT]:
            self.center_x += self.speed