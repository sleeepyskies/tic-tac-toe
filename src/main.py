from helpers import *

import sys
import typing

def main():
        
    # Main game loop
    while(game_active):
        current_turn += 1

        # Print the current game board to console
        print_board(game_board, current_turn)

        row, column = get_position(game_board)

        update_board(row, column, game_board, current_turn)

        game_active, winner = game_over(game_board)

    print_board(game_board, current_turn)
    game_end(current_turn, winner)