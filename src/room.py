
class Room:
    def __init__(self, name, description, inventory):
        self.name = name
        self.description = description
        self.inventory = inventory

    def gainItem(self, item):
        self.inventory.append(item)

    def loseItem(self, item):
        self.inventory.remove(item)
