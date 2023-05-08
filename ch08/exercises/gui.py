class Mario:
    def __init__(self, lives, coins, power_up):
        self.lives = lives
        self.coins = coins
        self.power_up = power_up

    def jump(self):
        # Jump action
        pass

    def move(self, direction):
        # Move action
        pass

    def collect_coin(self):
        self.coins += 1

    def use_power_up(self):
        self.power_up -= 1

class Enemy:
    def __init__(self, type, position, speed):
        self.type = type
        self.position = position
        self.speed = speed

    def move(self):
        # Move action
        pass

    def collide_with_mario(self):
        # Collision action with Mario
        pass

    def respawn(self):
        # Respawn action
        pass

class Coin:
    def __init__(self, value, position, is_visible):
        self.value = value
        self.position = position
        self.is_visible = is_visible

    def collect(self):
        self.is_visible = False

    def respawn(self):
        self.is_visible = True
