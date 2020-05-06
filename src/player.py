# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:

    def __init__(self, name, current_room, money, inventory):
        self.name = name
        self.current_room = current_room
        self.money = money
        self.inventory = inventory

    def pickUpItem(self, item):
        self.inventory.append(item)

    def dropItem(self, item):
        self.inventory.remove(item)
