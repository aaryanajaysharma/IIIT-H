from src.entity import Entity

class Building(Entity):
    def __init__(self, initial_health):
        super().__init__(initial_health)