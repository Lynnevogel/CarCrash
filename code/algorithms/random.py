from code.classes.board import Board
import random

def random_move(possible_boards: list[Board]) -> Board:
    if len(possible_boards) == 0:
        return None
    else:
        return random.choice(possible_boards)
