from board.Board import Board 
from abc import ABC, abstractmethod

class AbstractPlayer(ABC):
    """
    Represents a user player.
    """

    def __init__(self, symbol: str) -> None:
        """
        Constructor method. 
        """
        # Check player str is valid.
        if symbol != "X" and symbol != "O":
            raise ValueError(f"{symbol} is not a valid Symbol.")
        
        self.symbol = symbol

    @abstractmethod
    def make_move(self, board: Board | None = None) -> tuple[int, int]:
        """
        Gets the move the player would like to make from the user. Ensures the input is valid.
        """
        pass
    