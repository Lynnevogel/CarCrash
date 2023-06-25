from .depth_first import DepthFirst
from typing import Any, Optional
import copy 

class DepthFirstLimit(DepthFirst):

    def go(self) -> None:
        """
        Runs the algorithm until all possible states have been visited.
        """
        while self.states:
            # Get new state
            new_board = self.get_next_state()
            new_board_representation = new_board.get_representation(new_board)
            # Add new reperesentation to archive
            self.archive.add(new_board_representation)    
            if new_board.is_won():
                print("WON")
                # append current depth of winning configuration to list
                self.depth_list_won.append(len(new_board.directions))
                # get lowest winning depth
                self.lowest_depth_won = min(self.depth_list_won)
                # remove winning state from archive
                self.archive.remove(new_board_representation)
                # check whether solution is better than current best solution
                self.check_solution(new_board)
            # only look further if current depth not deeper than lowest_depth_won
            elif len(new_board.directions) < self.lowest_depth_won or len(self.depth_list_won) == 0:
                for car in new_board.cars:
                    child = copy.deepcopy(new_board)
                    # get possible board states from current car
                    moves, can_move = child.get_possible_moves(child, car)
                    # add possible board states to list of states
                    self.add_all_possible_states(can_move, moves)
        # print best solution and amount of moves
        print(f"lowest amount of moves: {self.number_of_moves[-1]}")
        print(f"moves of best solution: {self.best_solution}")
