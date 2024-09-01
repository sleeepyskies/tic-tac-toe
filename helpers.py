import sys

# Initialises the game, explains the rules, and determines the gamemode
def game_init():
    print("Welcome to console Tic Tac Toe!")
    print("Enter 1 to play against another player, and 2 to play against the computer.")

    gamemode = input()
    match gamemode:
        case "1":
            print("Playing against another player!")
        case "2":
            print("Playing against the computer!")
        case _:
            print("I'm sorry, you havent entered a valid input :(, exiting the game...)")
            game_end()

def game_over(board):
    return True

# Prints the win status and exits the game
def game_end(round):
    message : str = "X has won the game in " + str(round) + " rounds!"
    print(message)
    sys.exit(0)