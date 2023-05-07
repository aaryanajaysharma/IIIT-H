from src.entity import Entity

class Person(Entity):
    def __init__(self, initial_health):
        super().__init__(initial_health)