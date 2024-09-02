class StringHolder:
    """
    Class used to store any string constants used in the game.
    """

    INVALID_INPUT = "This input is invalid, please try again."

    WELCOME_MESSAGE = "Welcome to console Tic-Tac-Toe!"
    GAMEMODE_MESSAGE = "Enter 1 to play against another player, and 2 to play against the computer.\n"
    
    PLAYER_MODE = "Playing against another player!\n"
    COMPUTER_MODE = "Playing against the computer!\n"

    GAME_ENDED = "The game is over!\nFinal Board:"

    @staticmethod
    def game_over(win_round: int, winner: str) -> str:
        """
        Returns the str to print the final win message.
        """
        return f"The game is over. Player {winner} has won the game at round {win_round}.\nFinal Board:"
