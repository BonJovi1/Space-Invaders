import Missile


class Bullet2:
    def __init__(self, x, y, pyg_time, screen, ball):
        self.ball = ball
        self.x = x
        self.y = y
        self.time = pyg_time
        self.screen = screen
        

    def fire(self):
        self.screen.blit(self.ball, (self.x, self.y))
