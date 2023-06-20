import copy
from code.classes.board import Board
from typing import Optional, Any

class DepthFirst:
    """
    A Depth First algorithm...
    """
    def __init__(self, board: Board) -> None:
        self.board = copy.deepcopy(board)
        self.states = [copy.deepcopy(self.board)]
        self.existing_boards = [self.board.board]
        
        self.best_solution = None
        self.best_value = float('inf')

    def get_next_state(self) -> Board:    
        return self.states.pop()

    def get_all_possible_states(self, moves: list[Any], can_move: bool) -> None:
        if can_move:
            for move in moves:
                if move.board not in self.existing_boards:
                    self.states.append(move)
                    self.existing_boards.append(move.board)


    def check_solution(self, new_board: Optional[Board], depth: int) -> None:
        new_value = depth
        # print(f"New value: {new_value}")
        old_value = self.best_value
        print(f"old value: {self.best_value}")
        print(f"best value: {self.best_value}")
        print(f"depth: {depth}")

        if new_value <= old_value:
            self.best_solution = new_board
            self.best_value = new_value
        # print(f"best solution: {len(self.best_solution)}")


    def go(self) -> None:
        depth = 0
        
        while self.states:
            # print(f"aantal borden: {len(self.existing_boards)}")
            # print(f"states: {self.states}")  
            # print(f"aantal states: {len(self.states)}")
            new_board = self.get_next_state()
            depth += 1 
            print(f"best value: {self.best_value}")

            if new_board.is_won():
                # print("WON")
                self.check_solution(new_board, depth)
            else:
                for car in new_board.cars:
                    child = copy.deepcopy(new_board)
                    moves, can_move = child.get_possible_moves_2(child, car)
                    self.get_all_possible_states(moves, can_move)
        print(f"aantal directions: {len(new_board.directions)}")
