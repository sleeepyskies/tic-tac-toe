from player.AbstractPlayer import AbstractPlayer
from player.HumanPlayer import HumanPlayer
from player.AIPlayer import AIPlayer
from board.Board import Board
from renderer.Renderer import Renderer
from utils.StringHolder import StringHolder

class Game():
    """
    Responsible for conducting the overall game logic.
    """

    def __init__(self) -> None:
        """
        Constructor method.
        """
        # Player X is always a human
        self.playerX : AbstractPlayer = HumanPlayer("X")
        # Player O may be human or computer, init later
        self.playerO : AbstractPlayer = None

        # Set board attribute
        self.board : Board = Board()

        # Game starts at round 0
        self.__current_round : int = 0

        self.renderer = Renderer()

        self._init_game()
    
    def _init_game(self) -> None:
        """
        Used to initialise the game. 
        Determines the game mode to be played
        and sets up playerO attribute accordingly.
        """
        print(StringHolder.WELCOME_MESSAGE)
        print(StringHolder.GAMEMODE_MESSAGE)

        # Loops until valid input has been entered
        while True:
            # Get user input
            gamemode = input()
            match gamemode:
                case "1":
                    # Init playerO to be a human player, exit loop
                    self.playerO = HumanPlayer("O")
                    print(StringHolder.PLAYER_MODE)

                    break
                case "2":
                    # Init playerO to be a computer player, exit loop
                    self.playerO = AIPlayer("O")
                    print(StringHolder.COMPUTER_MODE)

                    break
                case _:
                    print(StringHolder.INVALID_INPUT)

    def play_game(self) -> None:
        """
        Main game loop. Stops only when the game has been won, or ended in a tie.
        """
        while True:
            # Increment round
            self.__current_round += 1

            # Print Board
            self.board.print_board()
            # Player X move
            self.__player_move(self.playerX)

            # check if X has won
            if self.board.game_over():
                break

            # Print Board
            self.board.print_board()
            # Player O move
            self.__player_move(self.playerO)

            # check if O has won
            if self.board.game_over():
                break

        print(StringHolder.game_over(self.__current_round, self.board.get_winner()))
        self.board.print_board()

        
    def __player_move(self, player: AbstractPlayer) -> None:
        """
        Handles logic for player placing move. Facilitates communication between Board and Player
        """
        while True:
            # check if player is AI or user
            if isinstance(player, AIPlayer):
                # player is AIPlayer
                row_x, col_x = player.make_move(self.board)
            else:
                # Player is a user
                row_x, col_x = player.make_move()

            try:
                # Move is valid, exit loop
                self.board.place_move(row_x, col_x, player.symbol)
                break
            except ValueError as e:
                # Move is invalid
                print(StringHolder.INVALID_INPUT + "3")

    def end_game(self) -> None:
        pass