import sys

# Initialises the game, explains the rules, and determines the gamemode
def game_init() -> None:
    print("Welcome to console Tic Tac Toe!")
    print("Enter 1 to play against another player, and 2 to play against the computer.")

    gamemode = input()
    match gamemode:
        case "1":
            print("Playing against another player! \n")
        case "2":
            print("Playing against the computer! \n")
        case _:
            print("I'm sorry, you havent entered a valid input :(, exiting the game...) \n")
            game_end(0)

    print("Player X may begin! \n")

# Prints the current game board to the command line
def print_board(board: list[str], current_round: int) -> None:
    # Determine current player turn
    player : str = "X" if current_round % 2 == 0 else "O"

    print("Round " + str(current_round) + ".")
    print("It is " + player + "'s turn.")

    for i in range(3):
        string_builder : str = "|"
        for j in range(3):
            string_builder += str(board[i*3 + j]) + "|"
        print(string_builder)

# Gets the position the current player wants to play their turn. Position stored as a tuple (i, j)
def get_position(game_board: list[str]) -> tuple[int, int]:
    # Get row
    print("What row would you like to play? (1-3)")
    row : int = int(input()) - 1
    if row not in range(3):
        game_end(0)

    # Get column
    print("What column would you like to play? (1-3)")
    column : int = int(input()) - 1
    if column not in range(3):
        game_end(0)

    # Check if the position is valid
    


def game_over(board: list[str]) -> bool:
    return True

# Prints the win status and exits the game
def game_end(round: int) -> None:
    # If round is 0, then user has entered incorrect input.
    if (round != 0):
        message : str = "X has won the game in " + str(round) + " rounds!"
        print(message)

    sys.exit(0)