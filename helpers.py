import sys

# Initialises the game, explains the rules, and determines the gamemode
def game_init() -> None:
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
            game_end(0)

# Prints the current game board to the command line
def print_board(board: list[str], current_round: int) -> None:
    for i in range(3):
        string_builder : str = "|"
        for j in range(3):
            string_builder += str(board[i*3 + j]) + "|"
        print(string_builder)


def game_over(board: list[str]) -> bool:
    return True

# Prints the win status and exits the game
def game_end(round: int) -> None:
    # If round is 0, then user has enetered incorrect input when deciding the game mode.
    if (round != 0):
        message : str = "X has won the game in " + str(round) + " rounds!"
        print(message)

    sys.exit(0)