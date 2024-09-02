from player.AbstractPlayer import AbstractPlayer
from random import randrange

from board.Board import Board

from time import sleep

class AIPlayer(AbstractPlayer):
    """
    Represents a computer opponent. Holds the logic for the computers moveset.
    """
    def __init__(self, symbol: str) -> None:
        """
        AIPlayer Constructor
        """
        # Call to parent constructor
        super().__init__(symbol)

    def make_move(self, board: Board | None = None) -> tuple[int, int]:
        """
        Gets the move the AI wants to make. Ensures the input is valid.

        """
        while True:
            row = randrange(3)
            col = randrange(3)
            
            if board.board[row * 3 + col] == " ":
                self.think_hard()
                return row, col
        
    def think_hard(self) -> None:
        sleep(0.75)
        print(".",end="", flush=True)
        sleep(0.75)
        print(".", end="", flush=True)
        sleep(0.75)
        print(".", flush=True)
        sleep(0.75)
