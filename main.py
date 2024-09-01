from helpers import *

# Used to check if game is still active
game_active = True
# Determines current turn
current_turn = 0
# Holds the board data
game_board = [" " for _ in range(9)]

game_init()

# Main game loop
while(game_active):
    game_active = game_over(game_board)