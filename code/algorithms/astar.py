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
        # queue
        self.states = [copy.deepcopy(self.board)]
        self.archive = [self.board.board]

        self.number_of_moves = []
        self.heuristic_values = []
        
        self.best_solution = None
        self.best_value = float('inf')

    def get_next_state(self) -> Board:    
        return self.states.pop(0)

    def get_all_possible_states(self, new_board: Board, can_move: bool, moves: list[Any]) -> None:
        """
        Adds states to the states list and keeps an archive of states that should not be 
        added to the states list.
        """
        if can_move:
            for move in moves:
                if move.board not in self.archive:
                    self.states.append(move)


    def check_solution(self, new_board: Optional[Board], heuristic_value: int) -> None:

        move_count = len(new_board.directions)

        if self.number_of_moves:
                print(f"heuristic values list: {self.heuristic_values}")
                lowest_value = min(self.heuristic_values)
                print(f"lowest_value: {lowest_value}")
                if heuristic_value < lowest_value:
                    self.number_of_moves.append(move_count)

                    self.heuristic_values.append(heuristic_value)

                    self.best_solution = []
                    self.best_solution.append(new_board.directions)
                    
        elif move_count > 0: 
            self.number_of_moves.append(move_count)
        
        print(heuristic_value)


    def blocking_cars(self, board: Board) -> int:

        blocking_cars = 0
        count = 0
        for car in board.cars:
            count += 1
            print(f"count: {count}")
            self.current_car = board.cars[car]
            # print(self.current_car)
            car_coordinates = self.current_car.car_coordinates
            print(f"car_coordinates: {car_coordinates}")
            # print(car_coordinates)
            
            red_car_coordinates = board.cars["X"].car_coordinates
            print(f"red_car_coordinates:{red_car_coordinates}")

            # car_coordinates[0][0] == 2 or car_coordinates[1][0] and 
            if car_coordinates != red_car_coordinates:
                if car_coordinates[0][0] == 2 or car_coordinates[1][0] == 2:

                    print(f"car_coordinates[0][0]: {car_coordinates[0][0]}")
                    print(f"car_coordinates[1][0]: {car_coordinates[1][0]}")
                    blocking_cars += 1
                    print(blocking_cars)

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
        print(f"amount_of_moves: {amount_of_moves}")
        blocking_cars = self.blocking_cars(new_board)
        print(f"blockingcars: {blocking_cars}")
        heuristic_value = amount_of_moves + blocking_cars
        self.heuristic_values.append(heuristic_value)
        return heuristic_value
    
    def go(self) -> None:
        depth = 0
        while self.states:
            new_board = self.get_next_state()
            self.archive.append(new_board.board)
            heuristic_value = self.heuristic(new_board)
            print(f"heuristic: {heuristic_value}")

            if new_board.is_won():
                print("WON")
                # remove winning state from archive
                self.archive.pop()
                # print(new_board.directions)
                self.check_solution(new_board, heuristic_value)
            else:
                for car in new_board.cars:
                    child = copy.deepcopy(new_board)
                    # get possible board states from current car
                    moves, can_move = child.get_possible_moves_2(child, car)
                    # add possible board states to list of states
                    self.get_all_possible_states(new_board, can_move, moves)
        print(f"lowest amount of moves: {self.number_of_moves[-1]}")
        print(f"moves of best solution: {self.best_solution}")

