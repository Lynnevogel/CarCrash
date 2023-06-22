from .depth_first import DepthFirst
from typing import Any

class BreadthFirst(DepthFirst):
    

    def get_next_state(self):
        """
        
        """
        return self.states.pop(0)

    def add_all_possible_states(self, new_board, can_move: bool, moves: list[Any]) -> None:
        """
        
        """
        if can_move:
            for move in moves:
                move_representation = move.get_representation_breadth(move)
                if move_representation not in self.archive:
                    self.states.append(move)
                    self.archive.add(move_representation)

        print(f"grootte archief: {len(self.archive)}")