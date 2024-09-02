class Player:
    """
    Represents a user player.
    """

    def __init__(self, symbol: str) -> None:
        """
        Constructor method. 
        """
        # Check player str is valid.
        if symbol != "X" or "O":
            raise ValueError(f"{symbol} is not a valid Symbol.")
        
        self.symbol = str

    def make_move(self) -> tuple[int, int]:
        pass