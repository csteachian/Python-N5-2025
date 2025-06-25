# Create a simple text-based adventure game called
# "The Mystery Mansion" where players can explore four
# different locations.
# Your program must demonstrate understanding of 1D arrays,
# input validation, and string concatenation.

# Your adventure takes place in a mysterious mansion with
# these four rooms:

# Entrance Hall - "A grand foyer with a crystal chandelier"
# Library - "Dusty bookshelves stretch from floor to ceiling"
# Kitchen - "Copper pots hang above an old stone hearth"
# Garden - "Overgrown vines twist around marble statues"

# 1. 1D Arrays
# Location Names Array: Store the four location names
# Location Descriptions Array: Store detailed descriptions for
# each location
# Available Commands Array: Store valid player commands
# (N, S, E, W, quit, help)

room = ['Entrance Hall','Library','Kitchen','Garden']
commands = ['N','S','E','W','quit','help']
description = [
    "A grand foyer with a crystal chandelier",
    "Dusty bookshelves stretch from floor to ceiling",
    "Copper pots hang above an old stone hearth",
    "Overgrown vines twist around marble statues"
]
current = 0
gameover = False

print("You are in the: "+room[current])
print(description[current])

# 2. Input Validation

# The valid directions are north (N), south (S),
# east (E) and west (W).
# If the user enters anything that isn’t a valid command
# or direction, display a helpful error message.
while gameover == False: 
    command = input("Enter command: ")
    while command not in commands:
        print("Error! Not a valid command.")
        command = input("Enter command: ")

    temppos = current
    validmove = False
    if command == "N":
        current -= 2
        validmove = True
    elif command == "S":
        current += 2
        validmove = True
    elif command == "E" and (current != 3 and current != 1):
        current += 1
        validmove = True
    elif command == "W" and current != 2:
        current -= 1
        validmove = True
    elif command == "quit":
        gameover = True
        validmove = True
    elif command == "help":
        print("Commands available are: N, S, E, W, help, quit\n")
        validmove = True

    if not validmove:
        print("You can't move in that direction")
        print()
        current = temppos

    # 3. String concatenation

    # You should combine the location name and description when
    # displaying this to the player.
    # You should create a personalised welcome message using the
    # player’s name

    print("You are in the: "+room[current])
    print(description[current])

