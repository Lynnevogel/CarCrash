from .depth_first import DepthFirst
from typing import Any, Optional
import copy 

class IterativeDeepening(DepthFirst):

    # - count depth in depthfirst 
    #     - onthoud Depth
    #     - is solution found, save depth
    #     - verderzoeken, maar niet als depth groter wordt dan gevonden depth 
    
    # function depthLimitedSearch(board, depthLimit, currentDepth):
    #     if currentDepth == depthLimit:
    #         if isGoalState(board):
    #             return board
    #         else:
    #             return null
    
    def check_solution(self, new_board, depth: int) -> None:
        """
        Checks whether the solution contains less moves than the current best solution.
        """
        move_count = len(new_board.directions)

        if self.number_of_moves:
                lowest_value = min(self.number_of_moves)
                if move_count < lowest_value:
                    self.number_of_moves.append(move_count)
                    self.best_solution = []
                    self.best_solution.append(new_board.directions)
        elif move_count > 0:
            self.number_of_moves.append(move_count)

        print(f"number of moves: {move_count}")

    def depth(self) -> None: 
        pass 

    def go(self) -> None:
        """
        Runs the algorithm until all possible states have been visited.
        """
        while self.states:
            new_board = self.get_next_state()
            new_board_representation = new_board.get_representation(new_board)
            self.archive.add(new_board_representation)
            self.depth += 1
            print(f"depth: {self.depth}")
            if new_board.is_won():
                print("WON")
                self.depth_list.append(self.depth)
                print(f"depth_list: {self.depth_list}")
                # remove winning state from archive
                self.archive.remove(new_board_representation)
                # check whether solution is better than current best solution
                self.check_solution(new_board, self.depth)
            else:
                for car in new_board.cars:
                    child = copy.deepcopy(new_board)
                    # get possible board states from current car
                    moves, can_move = child.get_possible_moves_2(child, car)
                    # add possible board states to list of states
                    self.add_all_possible_states(new_board, can_move, moves)
        # print best solution and amount of moves
        print(f"lowest amount of moves: {self.number_of_moves[-1]}")
        print(f"moves of best solution: {self.best_solution}")
