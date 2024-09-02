class Board:
    """
    Represents the board of the game. 
    """

    # List of all winning combinations of the game
    WIN_POSITIONS : list[tuple[int, int, int]] = list[
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    def __init__(self) -> None:
        """
        Constructor Method. Takes no arguments. Board represented as list of strings.
        " " -> Empty Position
        "X" -> Played by X
        "O" -> Player by O
        """
        # Init board with 9 empty slots
        self.board : list[str] = [" "] * 9

    def move_possible(self) -> bool:
        """
        Checks to see if there are any empty positions left to play.
        """
        return self.board.__contains__(" ")
    
    def place_move(self, column: int, row: int, player: str) -> None:
        """
        Places the players symbol ("X"/"O") at the given position.
        Throws error if this position is invalid or already taken.
        """ 
        # Check validity of position, throw error if invalid
        if column not in range(3) or row not in range(3):
            raise ValueError(f"The position {column}, {row} does not exist.")
        
        # Check if position is already taken
        if self.board[column * 3 + row] != " ":
            raise ValueError(f"The position {column}, {row} is already taken.")
        
        # Update Board
        self.board[column * 3 + row] = player

    def game_over(self) -> bool:
        """
        Checks to see if a player has won the game.
        """
        return self.get_winner() != " "
    
    def get_winner(self) -> str:
        """
        Returns the winner of the board. If nobody has won yet, returns " ".
        Assumes that only one player can win.
        """
        # Loop winning combinations, and check if a player has 
        for i, j, k in self.WIN_POSITIONS:
            if self.board[i] == self.board[j] == self.board[k] and self.board[i] != " ":
                return self.board[i]

    def print_board(self) -> None:
        """
        Function used to print the board to the console.
        TODO add fucntionality to render board.
        """
        for col in range(3):
            for row in range(3):
                string_builder = "|"
                string_builder += self.board[col * 3 + row]
            print(string_builder)