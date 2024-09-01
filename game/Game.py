from player.Player import Player 
from board.Board import Board

class Game:
    """
    Responsible for conducting the overall game logic.
    """

    def __init__(self) -> None:
        """
        Constructor method.
        """
        # Player X is always a human
        self.playerX : Player = Player()
        # Player O may be human or computer, init later
        self.playerO : Player = None

        # Set board attribute
        self.board : Board = Board()

        # Game starts at round 0
        current_round : int = 0

        self.init_game()
    
    def init_game() -> None:
        """
        Used to initialise the game. 
        Determines the game mode to be played
        and sets up playerO accordingly.
        """
        print("Welcome to console Tic Tac Toe!")
        print("Enter 1 to play against another player, and 2 to play against the computer.")

        gamemode = input()
        match gamemode:
            case "1":
                print("Playing against another player! \n")
                return None
            case "2":
                print("Playing against the computer! \n")
                return 
            case _:
                print("I'm sorry, you havent entered a valid input :(, exiting the game...) \n")

        print("Player X may begin! \n")