from .depth_first import DepthFirst
from code.classes.board import Board
import copy


class BreadthFirst(DepthFirst):
    def __init__(self, board: "Board") -> None:
        """
        Initializes BreadthFirst class and inherits the DephtFirst class.
        Precondtions:
        - board is a Board object of the current board.
        """
        self.board = copy.deepcopy(board)
        # Create the stack with the states
        self.states = [copy.deepcopy(self.board)]
        # Create archive
        self.archive = {self.board.get_representation(self.board, "breadthfirst")}
        self.number_of_moves = []
        # Create a set that stores the unique representations of all visited board states
        self.all_states = {self.board.get_representation(self.board, "breadthfirst")}

        self.win_count = 0
        # List to add best solution
        self.best_solution = []
        self.best_value = float('inf')

    def check_solution(self, new_board: "Board") -> None:
        """
        Checks whether the solution contains fewer moves than the current best solution.
        Preconditions:
        - new_board is a Board object which represents a board in the next state in the tree.
        """
        self.win_count += 1
        # Order solution
        solution = new_board.order_solution()
        move_count = len(solution)

        if self.win_count == 1:
            self.best_solution = solution

        if self.number_of_moves:
                # Get lowest number of moves 
                lowest_value = min(self.number_of_moves)
                # If current number of moves is lower than before, set as new best solution
                if move_count < lowest_value:
                    self.number_of_moves.append(move_count)
                    self.best_solution = []
                    self.best_solution = solution
        # For first solution
        elif move_count > 0:
            self.number_of_moves.append(move_count)

    def get_next_state(self) -> "Board":
        """
        Get the next state from the stack of states.
        Postconditions:
        - The next state, a Board object, is returned.
        """
        return self.states.pop(0)

    def add_all_possible_states(self, can_move: bool, moves: list["Board"]) -> None:
        """
        Adds possible board states to the archive
        Preconditions:
        - can_move is a boolean, which is true when the car can move.
        - moves is a list with the all the possible board states from the current board.
        """
        if can_move:
            for move in moves:
                move_representation = move.get_representation(move, "breadthfirst")
                if move_representation not in self.archive:
                    self.states.append(move)
                    self.archive.add(move_representation)

    def go(self) -> list[list[str | int]]:
        """
        Runs the algorithm until all possible board states have been visited.
        Postconditions:
        - A list with a Board object representing the best solution is returned.
        """
        # Until no board states left
        while self.states:
            # Get new board state
            new_board = self.get_next_state()
            new_board_representation = new_board.get_representation(new_board, "breadthfirst")
            
            # Add new state to archive
            self.archive.add(new_board_representation)
            self.all_states.add(new_board_representation)

            if new_board.is_won():
                print("Won")
                # Remove winning state from archive
                self.archive.remove(new_board_representation)
                # Check whether solution is better than current best solution
                self.check_solution(new_board)
            else:
                # Loop through cars in new state
                for car in new_board.cars:
                    child = copy.deepcopy(new_board)
                    # Get possible board states from current car
                    moves, can_move = child.get_possible_moves(child, car)
                    # Add possible board states to list of states
                    self.add_all_possible_states(can_move, moves)

        return self.best_solution
