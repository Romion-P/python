import os


# Display starting menu
def prompt():
    print("\t\tWelcome to Angel Engined\n\n\
You must collect all six items before fighting the boss.\n\n\
Moves:\t'go {direction}' (travel north, south, east, or west)\n\
\t'get {item}' (add nearby item to inventory)\n")

    input("Press Enter to continue...")


# Clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Map
Rooms = {
'Testing Chamber': {'East': 'Angel Engine Room #1'},
        'Angel Engine Room #1': {'West': 'Testing Chamber', 'East': 'Failed Experiments Room','North': 'Parts Room','South': 'Generator Room','Item': 'Key #1'},
        'Failed Experiments Room': {'West': 'Angel Engine Room #1', 'North': 'Dr. EverEvils Hideaway','Item':'Part #3'},
        'Dr. EverEvils Hideaway': {'South': 'Failed Experiments Room','Boss': 'Dr. EverEvil'},
        'Generator Room': {'East': 'Angel Engine Room #3', 'North': 'Angel Engine Room #1', 'Item': 'Part #2'},
        'Angel Engine Room #3': {'West': 'Generator Room','Item':'Key #3'},
        'Parts Room': {'South': 'Angel Engine Room #1', 'East': 'Angel Engine Room #2','Item':'Part #1'},
        'Angel Engine Room #2': {'West': 'Parts Room','Item':'Key #2'},
}


vowels = ['a', 'e', 'i', 'o', 'u']

# List to track inventory
inventory = []

# Tracks current room
current_room = 'Testing Chamber'

# Tracks last move
msg = ""

clear()
prompt()

# Gameplay loop
while True:

    clear()

    # Display player info
    print(f"You are in the {current_room}\nInventory : {inventory}\n{'-' * 30}")

    # Display msg
    print(msg)

    # Item indicator
    if "Item" in Rooms[current_room].keys():

        nearby_item = Rooms[current_room]["Item"]

        if nearby_item not in inventory:

            if nearby_item[-1] == 's':
                print(f"You see {nearby_item}")

            elif nearby_item[0] in vowels:
                print(f"You see an {nearby_item}")

            else:
                print(f"You see {nearby_item}")

    # Boss encounter
    if "Boss" in Rooms[current_room].keys():

        if len(inventory) < 6:
            print(f"You were not prepared and lost to {Rooms[current_room]['Boss']}.")
            break

        else:
            print(f"You freed the angels and used the Rail Cannon to defeat {Rooms[current_room]['Boss']}!")
            break

    # Accepts player's move as input
    user_input = input("Enter your move:\n")


    next_move = user_input.split(' ')


    action = next_move[0].title()

    item = "Item"
    direction = "null"


    if len(next_move) > 1:
        item = next_move[1:]
        direction = next_move[1].title()

        item = " ".join(item).title()

    # Moving between rooms
    if action == "Go":

        try:
            current_room = Rooms[current_room][direction]
            msg = f"You travel {direction}"

        except:
            msg = "You can't go that way."

    # Picking up items
    elif action == "Get":
        try:
            if item == Rooms[current_room]["Item"]:

                if item not in inventory:

                    inventory.append(Rooms[current_room]["Item"])
                    msg = f"{item} retrieved!"

                else:
                    msg = f"You already have the {item}"

            else:
                msg = f"Can't find {item}"
        except:
            msg = f"Can't find {item}"

    # Exit program
    elif action == "Exit":
        break

    # Any invalid commands
    else:
        msg = "Invalid command"