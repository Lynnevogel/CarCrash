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
        Checks whether the solution contains less moves than the current best solution.
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

    def go(self) -> None:
        """
        Runs the algorithm until all possible states have been visited.
        """
        while self.states:
            new_board = self.get_next_state()
            new_board_representation = new_board.get_representation(new_board)
            self.archive.add(new_board_representation)
            print(f"states: {len(self.states)}")
            if new_board.is_won():
                print("WON")
                # remove winning state from archive
                self.archive.remove(new_board_representation)
                # check whether solution is better than current best solution
                self.check_solution(new_board)
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
