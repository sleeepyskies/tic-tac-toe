from utils.StringHolder import StringHolder
from player.AbstractPlayer import AbstractPlayer
from board.Board import Board 

class HumanPlayer(AbstractPlayer):
    """
    Represents a user player.
    """

    def __init__(self, symbol: str) -> None:
        """
        Constructor method. 
        """
        super().__init__(symbol)


    def make_move(self, board: Board | None = None) -> tuple[int, int]:       
        """
        Gets the move the player would like to make from the user. Ensures the input is valid.
        """
        row : int = 0
        col : int = 0

        # Get column
        while True:
            row_str : str = input("Player " + self.symbol + "'s turn.\n What row would you like to play? (1-3)")

            if self.__check_input(row_str):
                # Input is valid, exit loop
                row = int(row_str) - 1
                break

        # Get row
        while True:
            col_str : str = input("What column would you like to play? (1-3)")

            if self.__check_input(col_str):
                # Input is valid, exit loop
                col = int(col_str) - 1
                break

        return (row, col)

    def __check_input(self, value: str) -> bool:
        """
        Helper function used to check whether a players position input is valid.
        """
        # Catch error if input is not a number
        try:
            int(value)
        except ValueError as e:
            print(StringHolder.INVALID_INPUT + "1")
            return False

        # Check if value is in range(3)
        if int(value) - 1 not in range(3):
            print(StringHolder.INVALID_INPUT + "2")
            return False

        # Input is valid
        return True