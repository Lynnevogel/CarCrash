from .depth_first import DepthFirst
from code.classes.board import Board
from typing import Any
import copy
from typing import Optional, Any


class BreadthFirst(DepthFirst):
    def __init__(self, board: Board) -> None:
        self.board = copy.deepcopy(board)
        self.states = [copy.deepcopy(self.board)]
        self.archive = {self.board.get_representation(self.board)}
        self.number_of_moves = []
        self.all_states = {self.board.get_representation(self.board)}

        self.win_count = 0
        self.best_solution = []
        self.best_value = float('inf')
    
    def check_solution(self, new_board: Optional[Board]) -> None:
        """
        Checks whether the solution contains less moves than the current best solution.
        """
        self.win_count += 1
        solution = new_board.order_solution()
        move_count = len(solution)

        if self.win_count == 1:
            self.best_solution = solution

        if self.number_of_moves:
                lowest_value = min(self.number_of_moves)
                if move_count < lowest_value:
                    self.number_of_moves.append(move_count)
                    self.best_solution = []
                    self.best_solution.append(solution)
        elif move_count > 0:
            self.number_of_moves.append(move_count)

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

    def go(self) -> None:
        """
        Runs the algorithm until all possible states have been visited.
        """
        while self.states:
            new_board = self.get_next_state()
            new_board_representation = new_board.get_representation(new_board)
            self.archive.add(new_board_representation)
            self.all_states.add(new_board_representation)
            # print(f"states: {len(self.states)}")
            if new_board.is_won():
                print("WON")
                # remove winning state from archive
                self.archive.remove(new_board_representation)
                # check whether solution is better than current best solution
                self.check_solution(new_board)
                print(f"solution found (breadth first): {len(self.best_solution)}, {self.best_solution}")
            else:
                for car in new_board.cars:
                    child = copy.deepcopy(new_board)
                    # get possible board states from current car
                    moves, can_move = child.get_possible_moves_2(child, car)
                    # add possible board states to list of states
                    self.add_all_possible_states(new_board, can_move, moves)
        
        # print best solution and amount of moves
        # print(f"lowest amount of moves (breadth first): {self.number_of_moves[-1]}")
        # print(f"moves of best solution (breadth first): {self.best_solution}")

        return self.best_solution
        