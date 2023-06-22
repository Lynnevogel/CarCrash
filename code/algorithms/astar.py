import copy
from code.classes.board import Board
from typing import Optional, Any

class AStar:
    """
    AStar algorithm...
    """
    def __init__(self, board: Board) -> None:
        # startstate
        self.board = copy.deepcopy(board)
        self.states = [copy.deepcopy(self.board)]
        self.existing_boards = [self.board.board]
        self.number_of_moves = []
        
        self.best_solution = None
        self.best_value = float('inf')

    def get_next_state(self) -> Board:    
        return self.states.pop(0)

    def get_all_possible_states(self, moves: list[Any], can_move: bool) -> None:
        if can_move:
            for move in moves:
                if move.board not in self.existing_boards:
                    self.states.append(move)
                    self.existing_boards.append(move.board)


    def check_solution(self, new_board: Optional[Board], depth: int, heuristic_value: int) -> None:

        move_count = len(new_board.directions)
        
        if self.number_of_moves:
                print(f"test: {self.number_of_moves}")
                lowest_value = min(move[1] for move in self.number_of_moves)
                if heuristic_value < lowest_value:
                    self.number_of_moves.append([new_board.directions, move_count])
        elif move_count > 0: 
            self.number_of_moves.append([new_board.directions, move_count])
        
        print(move_count)


    def blocking_cars(self, board: Board) -> int:

        blocking_cars = 0
        print(f"blocking_cars_0: {blocking_cars}")

        for car in board.cars:
            self.current_car = board.cars[car]
            # print(self.current_car)
            car_coordinates = self.current_car.car_coordinates
            # print(car_coordinates)
            
            red_car_coordinates = board.cars["X"].car_coordinates
            # Find end coordinates of red car
            x_start = red_car_coordinates[1][1]

            # Check if cars on the right of red car    
            while x_start + 1 < self.board.dim:
                x_start += 1
                if board.board[2][x_start] != "-":
                    blocking_cars += 1

        print(f"blockingcars: {blocking_cars}")
        if blocking_cars == 0:
            return 0
        else: 
            return blocking_cars

    def amount_of_moves(self, new_board: Board) -> int:
        if len(new_board.directions) == 0:
            return 0
        else: 
            return len(new_board.directions)

    def heuristic(self, new_board: Board) -> int:
        amount_of_moves = self.amount_of_moves(new_board)
        print(f"moves: {amount_of_moves}")
        blocking_cars = self.blocking_cars(new_board)
        print(f"blockingcars: {blocking_cars}")
        heuristic_value = amount_of_moves + blocking_cars
        return heuristic_value
    
    def go(self) -> None:
        depth = 0
        while self.states:
            new_board = self.get_next_state()
            heuristic_value = self.heuristic(new_board)
            depth += 1
            if new_board.is_won():
                print("WON")
                # print(new_board.directions)
                self.check_solution(new_board, depth, heuristic_value)
            else:
                for car in new_board.cars:
                    child = copy.deepcopy(new_board)
                    moves, can_move = child.get_possible_moves_2(child, car)
                    self.get_all_possible_states(moves, can_move)
        print(self.number_of_moves)

