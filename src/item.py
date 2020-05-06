
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        print(self.name + ', ' + self.description)

    def on_take(self, item):
        print("You have picked up " + item)


class Treasure(Item):
    def __init__(self, name, description, worth):
        super(name, description)
        self.worth = worth

    def sell(self, item, player):
        player.money += self.worth
        player.inventory.remove(item)

