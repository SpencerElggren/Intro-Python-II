from src.room import Room
from src.player import Player
from src.item import Item, Treasure

# Declare all the rooms

items = {
    'Poo-stick': Item('Poo-stick', 'Beware the fury of the Poo-stick'),
    'Candlestick': Treasure('Candlestick', 'Extremely old', 5),
    'Blob': Item('Blob', 'What is this?'),
    'Telescope': Item('Telescope', 'Still somewhat functional'),
    'Wooden-cup': Item('Wooden-Cup', 'Worthless or priceless?')
}

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", ['Poo-stick']),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ['Candlestick']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ['Telescope']),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ['Blob']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ['Wooden-Cup']),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

is_game_over = False

rand = Player('rand', room['outside'], [])

# while not is_game_over:
#     print(rand.current_room.name)
#     print(rand.current_room.description)
#     if rand.current_room.inventory:
#         print('Item available')
#     what = input('What do? ')
#     if what == 'n':
#         try:
#             rand.current_room = rand.current_room.n_to
#         except:
#             print('Direction unavailable')
#     elif what == 'e':
#         try:
#             rand.current_room.e_to
#         except:
#             print('Direction unavailable')
#     elif what == 's':
#         try:
#             rand.current_room.s_to
#         except:
#             print('Direction unavailable')
#     elif what == 'w':
#         try:
#             rand.current_room.w_to
#         except:
#             print('Direction unavailable')
#     elif what == 'q':
#         is_game_over = True
#     elif what == f'get {item}':
#
#     # elif what == 'get item':
#     #     rand.pickUpItem(rand.current_room.inventory[0])
#     #     rand.current_room.loseItem()
#     # elif what == 'drop item':
#     #     rand.dropItem(rand.current_room.inventory[0])
#     #     rand.current_room.gainItem(rand.current_room.inventory[0])
#     elif what == 'inventory':
#         for i in rand.inventory:
#             print(i.name + ', ' + i.description)
#     else:
#         print('Not available')


while not is_game_over:
    print(rand.current_room.name)
    print(rand.current_room.description)
    if rand.current_room.inventory:
        print('Items available:')
        for i in rand.current_room.inventory:
            print(i)
    what = input('What do? ')
    if len(what) == 1:
        if what == 'n':
            try:
                rand.current_room = rand.current_room.n_to
            except:
                print('Direction unavailable')
        elif what == 'e':
            try:
                rand.current_room.e_to
            except:
                print('Direction unavailable')
        elif what == 's':
            try:
                rand.current_room.s_to
            except:
                print('Direction unavailable')
        elif what == 'w':
            try:
                rand.current_room.w_to
            except:
                print('Direction unavailable')
        elif what == 'q':
            is_game_over = True
        elif what == 'i':
            for i in rand.inventory:
                print(items[i].name + ', ' + items[i].description)

    elif len(what.split()) == 2:
        if what.split()[0] == 'get' or what.split()[0] == 'take':
            getItem = what.split()[1]
            if getItem in rand.current_room.inventory:
                rand.pickUpItem(getItem)
                rand.current_room.loseItem(getItem)

            else:
                print(f"{getItem} is not in here")
        elif what.split()[0] == 'drop':
            dropItem = what.split()[1]
            if dropItem in rand.inventory:
                rand.dropItem(dropItem)
                rand.current_room.gainItem(dropItem)

    elif what == 'inventory':
        for i in rand.inventory:
            print(items[i].name + ', ' + items[i].description)
    else:
        print('Invalid command')
