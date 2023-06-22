from .depth_first import DepthFirst
from typing import Any

class BreadthFirst(DepthFirst):

    def get_next_state(self):
        """
        
        """
        return self.states.pop(0)

    def get_all_possible_states(self, new_board, can_move: bool, moves: list[Any]) -> None:
        """
        
        """
        if can_move:
            for move in moves:
                if move.board not in self.archive:
                    self.states.append(move)
                    self.archive.append(move.board)
