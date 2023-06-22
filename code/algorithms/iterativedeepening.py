# from .depth_first import DepthFirst
# from typing import Any, Optional
# import copy 

# class IterativeDeepening(DepthFirst):
#     """
#     An Iterative Deepening algorithm...
#     """
#     def depth_limited_search(self, board, depth_limit: int):
#         if depth_limit == 0:
#             if board.is_won():
#                 return board
#             else:
#                 return None
#         else:
#             for car in board.cars:
#                 child = copy.deepcopy(board)
#                 moves, can_move = child.get_possible_moves_2(child, car)
#                 for move in moves:
#                 for car in new_board.cars:
#                     child = copy.deepcopy(new_board)
#                     # get possible board states from current car
#                     moves, can_move = child.get_possible_moves_2(child, car)
#                     # add possible board states to list of states
#                     self.add_all_possible_states(new_board, can_move, moves)
#                     if result is not None:
#                         return result
#             return None



#     def iterative_deepening_search(self) -> None:
#         depth_limit = 0
#         while True:
#             result = self.depth_limited_search(self.board, depth_limit)
#             if result is not None:
#                 self.best_solution = result.directions
#                 self.best_value = len(result.directions)
#                 break
#             depth_limit += 1

#         print(f"lowest amount of moves: {self.best_value}")
#         print(f"moves of the best solution: {self.best_solution}")

import copy
from code.classes.board import Board
from typing import Optional, Any


class IterativeDeepening:
    """
    A Depth First algorithm...
    """
    def __init__(self, board: Board) -> None:
        self.board = copy.deepcopy(board)
        self.states = [copy.deepcopy(self.board)]
        self.archive = {self.board.get_representation(self.board)}
        self.number_of_moves = []

        self.depth_list_won = []
        self.lowest_depth_won = 0
    
        self.best_solution = []
        self.best_value = float('inf')

    def get_next_state(self) -> Board:
        """
        Returns the last added state from the states list.
        """
        return self.states.pop()

    def add_all_possible_states(self, new_board: Board, can_move: bool, moves: list[Any]) -> None:
        """
        Adds states to the states list and keeps an archive of states that should not be 
        added to the states list.
        """
        
        if can_move:
            for move in moves:
                if move.get_representation(move) not in self.archive and len(move.directions) < 40:
                    self.states.append(move)

    def check_solution(self, new_board: Optional[Board]) -> None:
        """
        Checks whether the solution contains fewer moves than the current best solution.
        """
        move_count = len(new_board.directions)
        print(f"move count: {move_count}")

        if self.number_of_moves:
                lowest_value = min(self.number_of_moves)
                if move_count < lowest_value:
                    self.number_of_moves.append(move_count)
                    self.best_solution = []
                    self.best_solution.append(new_board.directions)
        elif move_count > 0:
            self.number_of_moves.append(move_count)

        print(f"number of moves: {move_count}")

    def iterativeDeepening(self) -> None:
        """
        Applies the iterative deepening algorithm to the depth-first search.
        """
        maxDepth = 1
        while True:
            print(f"Max Depth: {maxDepth}")
            if self.DFS(self.board, maxDepth):
                return
            maxDepth += 1

    def DFS(self, currentNode: Board, depth: int) -> bool:
        """
        Performs a depth-limited search (DFS) with the given depth.
        # """
        # if depth == 0:
        #     if currentNode.is_won():
        #         self.check_solution(currentNode)
        #         return True
        #     return False

        for car in currentNode.cars:
            child = copy.deepcopy(currentNode)
            moves, can_move = child.get_possible_moves_2(child, car)
            self.add_all_possible_states(currentNode, can_move, moves)

        while self.states:
            new_board = self.get_next_state()
            new_board_representation = new_board.get_representation(new_board)
            self.archive.add(new_board_representation)
            print(f"states: {len(self.states)}")

            if new_board.is_won():
                print("WON")
                self.archive.remove(new_board_representation)
                self.check_solution(new_board)
                return True

            if self.DFS(new_board, depth - 1):
                return True

        return False

    def go(self) -> None:
        """
        Runs the iterative deepening depth-first search algorithm until all possible states have been visited.
        """
        self.iterativeDeepening()
        
        # Print the best solution and the number of moves
        print(f"lowest amount of moves: {self.number_of_moves[-1]}")
        print(f"moves of best solution: {self.best_solution}")
