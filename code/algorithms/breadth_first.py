from .depth_first import DepthFirst
from typing import Any

class BreadthFirst(DepthFirst):

    def get_next_state(self):
        return self.states.pop(0)
    
    def get_all_possible_states(self, moves: list[Any], can_move: bool) -> None:
        if can_move:
            for move in moves:
                if move.board not in self.existing_boards:
                    self.states.append(move)
                    self.existing_boards.append(move.board)