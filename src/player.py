# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:

    def __init__(self, name, current_room, money, inventory):
        self.name = name
        self.current_room = current_room
        self.money = money
        self.inventory = inventory

    def pickUpItem(self, item, room):
        self.inventory.append(item)
        room.inventory.remove(item)
        print(f"{item} picked up")

    def dropItem(self, item, room):
        self.inventory.remove(item)
        room.inventory.append(item)
        print(f"{item} dropped")

    def checkInv(self, items):
        print(f"Money: {self.money}")
        for i in self.inventory:
            print(items[i].name + ', ' + items[i].description)
