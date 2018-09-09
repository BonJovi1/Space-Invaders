class Spaceship:

    def __init__(self, a, b, spaceship, screen):
        self.a = a
        self.b = b
        self.spaceship = spaceship
        self.screen = screen

    def ship(self):
        self.screen.blit(self.spaceship, (self.a, self.b))  # placing the ship
