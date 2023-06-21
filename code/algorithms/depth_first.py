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
        self.number_of_moves = []
        
        self.best_solution = None
        self.best_value = float('inf')

    def get_next_state(self) -> Board: 
        return self.states.pop()

    def get_all_possible_states(self, new_board: Board, can_move: bool, moves: list[Any]) -> None:
        self.existing_boards.append(new_board.board)
        if new_board.is_won():
            self.existing_boards.pop()

        if can_move:
            for move in moves:
                if move.board not in self.existing_boards:
                    self.states.append(move)
                    self.existing_boards.append(move.board)


    def check_solution(self, new_board: Optional[Board], depth: int) -> None:

        move_count = len(new_board.directions)
        
        if self.number_of_moves:
                lowest_value = min(move[1] for move in self.number_of_moves)
                print(f"lowest_value: {lowest_value}")
                if move_count < lowest_value:
                    self.number_of_moves.append([new_board.directions, move_count])
        elif move_count > 0: 
            self.number_of_moves.append([new_board.directions, move_count])
        


    def go(self) -> None:
        depth = 0
        # while self.states:
        for i in range(3):
            print(i)
            new_board = self.get_next_state()
            depth += 1
            if new_board.is_won():
                print("WON")
                # print(new_board.directions)

                self.check_solution(new_board, depth)
                # print(f"states: {self.states}")
            else:
                for car in new_board.cars:
                    child = copy.deepcopy(new_board)
                    moves, can_move = child.get_possible_moves_2(child, car)
                    self.get_all_possible_states(moves, can_move)
        print(self.number_of_moves)
