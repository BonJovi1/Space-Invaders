class Aliens:
    def __init__(self, x, y, pyg_time, screen, arpita, alien):
        self.x = x
        self.y = y
        self.time = pyg_time
        self.new = True
        self.arpita = arpita
        self.screen = screen
        self.alien = alien

    def spawn(self):
        self.screen.blit(self.arpita, (self.x, self.y))

    def spawn_again(self):
        self.screen.blit(self.alien, (self.x, self.y))
