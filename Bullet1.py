import Missile


class Bullet1:
    def __init__(self, x, y, pyg_time, screen, lightsaber):
        self.x = x
        self.y = y
        self.time = pyg_time
        self.screen = screen

        self.lightsaber = lightsaber

    def fire(self):
        self.screen.blit(self.lightsaber, (self.x, self.y))
