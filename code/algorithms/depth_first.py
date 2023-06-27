import copy
from code.classes.board import Board
from typing import Union


class DepthFirst:
    """
    A Depth First algorithm.
    """
    def __init__(self, board: "Board") -> None:
        """
        Initializes DepthFirst class.
        Preconditions:
        - board is a Board object with the current board
        """
        self.board = copy.deepcopy(board)
        # Create the stack with the states
        self.states = [copy.deepcopy(self.board)]
        # Create archive
        self.archive = {self.board.get_representation(self.board)}
        self.number_of_moves: list[int] = []
        # Create a set that stores the unique representations of all visited board states
        self.all_states = {self.board.get_representation(self.board)}

        # List to add depth when a winning configuration is found
        self.depth_list_won: list[int] = []
        self.lowest_depth_won = 0

        self.best_solution: list[list[str|int]] = []
        self.best_value = float('inf')

    def get_next_state(self) -> "Board":
        """
        Get the next state from the stack of states.
        Postconditions:
        - the next state, a Board object, is returned
        """
        return self.states.pop()

    def add_all_possible_states(self, can_move: bool, moves: list["Board"]) -> None:
        """
        Adds possible board states to the archive
        Preconditions:
        - can_move is a boolean, which is true when the car can move
        - moves is a list with the all the possible board states from the current board
        """
        if can_move:
            for move in moves:
                 if move.get_representation(move) not in self.archive and len(move.move_set) < 100:
                    self.states.append(move)

    def check_solution(self, new_board: "Board") -> None:
        """
        Checks whether the solution contains fewer moves than the current best solution.
        Preconditions:
        - new_board is a Board object which represents a board in the next state in the tree
        """
        # Order solution
        solution = new_board.order_solution()
        print(solution)
        move_count = len(solution)
        print(move_count)
        print(f"number :{self.number_of_moves}")

        if self.number_of_moves:
                print("hi")
                # Get lowest number of moves 
                lowest_value = min(self.number_of_moves)
                print(f"Low: {lowest_value}")
                # If current number of moves is lower than before, set as new best solution
                if move_count < lowest_value:
                    self.number_of_moves.append(move_count)
                    self.best_solution = []
                    self.best_solution.append(solution)
        # For first solution
        elif move_count > 0:
            self.number_of_moves.append(move_count)

    def go(self) -> None:
        """
        Runs the algorithm until all possible board states have been visited.
        """
        # Until no board states left
        while self.states:
            # Get new board state
            new_board = self.get_next_state()
            new_board_representation = new_board.get_representation(new_board)

            # Add new state to archive
            self.archive.add(new_board_representation)
            self.all_states.add(new_board_representation)
            if new_board.is_won():
                print("WON")
                # Remove winning state from archive
                self.archive.remove(new_board_representation)
                # Check whether solution is better than current best solution
                self.check_solution(new_board)
            else:
                for car in new_board.cars:
                    child = copy.deepcopy(new_board)
                    # Get possible board states from current car
                    moves, can_move = child.get_possible_moves(child, car)
                    # Add possible board states to list of states
                    self.add_all_possible_states(can_move, moves)


    def generate_output(self) -> tuple[int, int, list[list[str|int]]]:
        """
        Return generated ouput from every run.
        Postconditions: 
        - number_of_moves is the amount of moves made and is an integer.
        - number_of_states if the amound of states visited and is an integer.
        - solution is a nested list with a string and an integers.
        """
        number_of_moves = len(self.best_solution)
        number_of_states = len(self.all_states)
        if len(self.best_solution) > 1:
            solution = self.best_solution
        else:
            solution = self.best_solution[0]
            number_of_moves = len(self.best_solution[0])
        return number_of_moves, number_of_states, solution
