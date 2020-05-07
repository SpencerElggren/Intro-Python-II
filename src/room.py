
class Room:
    def __init__(self, name, description, inventory, obstacle):
        self.name = name
        self.description = description
        self.inventory = inventory
        self.obstacle = obstacle

    def destroyObstacle(self):
        self.obstacle.pop()
