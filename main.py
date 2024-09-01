from helpers import *

import sys

# Used to check if game is still active
game_active : bool = True
# Determines current turn
current_turn : int = 0
# Holds the board data
game_board : list[str] = [" " for _ in range(9)]

game_init()

# Main game loop
while(game_active):
    current_turn += 1

    # Print the current game board to console
    print_board(game_board, current_turn)

    row, column = get_position(game_board)

    update_board(row, column, game_board, current_turn)

    game_active = not(game_over(game_board))

game_end(current_turn)