from player.Player import Player
from player.AIPlayer import AIPlayer
from board.Board import Board
from utils.StringHolder import StringHolder

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
    
    def init_game(self) -> None:
        """
        Used to initialise the game. 
        Determines the game mode to be played
        and sets up playerO attribute accordingly.
        """
        print(StringHolder.WELCOME_MESSAGE)
        print(StringHolder.GAMEMODE_MESSAGE)

        # Loops until valid input has been entered
        input_valid: bool = False
        while(not(input_valid)):
            # Get user input
            gamemode = input()
            match gamemode:
                case "1":
                    # Init playerO to be a human player
                    self.playerO = Player()

                    print(StringHolder.PLAYER_MODE)
                case "2":
                    # Init playerO to be a computer player
                    self.playerO = AIPlayer()

                    print(StringHolder.COMPUTER_MODE)
                case _:
                    print(StringHolder.INVALID_INPUT)

            print("Player X may begin! \n")