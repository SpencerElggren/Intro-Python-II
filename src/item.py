
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        print(self.name + ', ' + self.description)


class Treasure(Item):
    def __init__(self, name, description, worth):
        super().__init__(name, description)
        self.worth = worth

    def sell(self, item, player):
        player.money += self.worth
        player.inventory.remove(item)


class Utility(Item):
    def __init__(self, name, description, use, durability):
        super().__init__(name, description)
        self.use = use
        self.durability = durability

    def use(self, room):
        self.durability -= 1
        room.obstacle.pop()


class Weapon(Item):
    def __init__(self, name, description, speed, damage):
        super().__init__(name, description)
        self.speed = speed
        self.damage = damage
