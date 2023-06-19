from code.classes.board import Board
from typing import Union
import random

def random_move(possible_boards: list[Board]) -> Union[Board, None]:
    if len(possible_boards) == 0:
        return None
    else:
        return random.choice(possible_boards)
