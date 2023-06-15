from code.classes.board import Board
import random

def random_move(possible_boards: list[Board]) -> Board:
    # Return random board
    return random.choice(possible_boards)
