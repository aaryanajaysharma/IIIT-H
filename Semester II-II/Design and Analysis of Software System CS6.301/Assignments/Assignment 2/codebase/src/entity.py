class Entity:
    def __init__(self, initial_health):
        self.health = initial_health
        self.initial_health = initial_health
        self.alive = True
        self.colour = ''

    def set_health(self, health):
        self.health = health

    def find_colour(self):
        if self.health >= self.initial_health / 2:
            self.colour = 'G'
        elif self.health >= self.initial_health / 5:
            self.colour = 'Y'
        elif self.health > 0:
            self.colour = 'R'
        else:
            self.alive = False
            self.colour = 'N'