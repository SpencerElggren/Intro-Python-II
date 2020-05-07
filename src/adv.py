from src.room import Room
from src.player import Player
from src.item import Item, Treasure, Utility, Weapon

valid_commands = [
    'n', 'e', 'w', 's', 'i', 'get [ITEM]', 'use [ITEM]', 'sell [ITEM]', 'inventory', 'q'
]

items = {
    'Poo-stick': Weapon('Poo-stick', 'Beware the fury of the Poo-stick', 2, 1),
    'Candlestick': Treasure('Candlestick', 'Extremely old', 5),
    'Blob': Item('Blob', 'What is this?'),
    'Skull': Item('Skull', 'Probably from the last person to fall in'),
    'Telescope': Item('Telescope', 'Still somewhat functional'),
    'Wooden-cup': Item('Wooden-Cup', 'Worthless or priceless?'),
    'Crowbar': Utility('Crowbar', 'It is definitely a reference to something', 'Use: Break obstacles', 10)
}

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons.", ['Poo-stick'], ['large rock']),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ['Candlestick'], []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ['Telescope'], []),

    'abyss': Room('The Abyss', """Now you have done it. You stared into the abyss too long,
felt something look back, and you fell in. You wish you were dead.""", ['Skull'], []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ['Blob'], ['weak door']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ['Wooden-Cup'], []),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['overlook'].n_to = room['abyss']
room['overlook'].e_to = room['abyss']
room['overlook'].w_to = room['abyss']
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

rand = Player('rand', room['outside'], 0,  ['Crowbar'])

while not is_game_over:
    print('')
    print(rand.current_room.name)
    print(rand.current_room.description)
    if rand.current_room.obstacle:
        print(f"There is a {rand.current_room.obstacle[0]} in the way")
    if rand.current_room.inventory:
        print('Items available:')
        for i in rand.current_room.inventory:
            print(i)
    print('')
    what = input('What do? ')
    if len(what) == 1:
        if what == 'n' or what == 'e' or what == 's' or what == 'w':
            if not rand.current_room.obstacle:
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
            elif rand.current_room.obstacle:
                print(f"There is a {rand.current_room.obstacle[0]} in the way")

        elif what == 'q':
            is_game_over = True
        elif what == 'i':
            rand.checkInv(items)

    elif len(what.split()) == 2:
        action = what.split()[0]
        enacted = what.split()[1]
        if action == 'get' or action == 'take':
            if enacted in rand.current_room.inventory:
                rand.pickUpItem(enacted, rand.current_room)
            else:
                print(f"{enacted} is not in here")

        elif action == 'drop':
            if enacted in rand.inventory:
                rand.dropItem(enacted, rand.current_room)
            else:
                print("Item not in inventory")

        elif action == 'use':
            if enacted in rand.inventory:
                if enacted == 'Crowbar':
                    if rand.current_room.obstacle:
                        rand.current_room.destroyObstacle()
                        items[enacted].durability -= 1
                        print("Obstacle destroyed")
                        print(f'{enacted} durability: {items[enacted].durability}')
                    else:
                        print("No obstacle")
            else:
                print("Item not in inventory")

        elif action == 'sell':
            if enacted in rand.inventory:
                items[enacted].sell(enacted, rand)
                print(f"Money: {rand.money}")

    elif what == 'inventory':
        rand.checkInv(items)

    else:
        print('Invalid command')
        print('Valid commands:')
        for i in valid_commands:
            print(i)
