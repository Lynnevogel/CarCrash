from .cars import Car
import random
import copy
from typing import Literal
import csv
import re
import pickle
from code.visualization.color_blocks import visualize_board


class Board:
    def __init__(self, game_name: str) -> None:
        """
        Initializes the Rush Hour game.
        Preconditions:
        - game_name is a string the format must be 'NxN_M', where N and M are positive integers
        """
        # Extract dimension from name
        self.dim: int = int(game_name.strip().split("x")[0])
        # Initialize board
        self.board = [["-" for _ in range(self.dim)] for _ in range(self.dim)]
        self.cars: dict[str, Car] = {}
        self.directions: list[list[str|int]] = []
        self.move_set: set[str] = set()
        self.last_move = ""
        self.set_boards: set[str] = set()

         # Load data
        self.load_cars(f"gameboards/Rushhour{game_name}.csv")
        self.current_car: Car = self.cars['X']

        # Intialize first board
        self.load_board()
        self.add_cars(self.board)
        self.print_board()
    
    def __repr__(self) -> str:
        return f"{self.print_board()}"

    def get_representation(self, board: "Board") -> str:
        """
        Get the representation of the board
        Preconditions:
        - board is a Board object containing the current board
        Postconditions:
        - A string representation of the board and ... is returned
        """
        representation = re.sub(r"[^\w-]", "", str(board))
        representation = re.sub(r"'", "", representation)
        return representation+str(len(board.directions))
    
    def get_representation_breadth(self, board: "Board") -> str:
        """
        Get the representation of the board in breadth first search
        Preconditions:
        - board is a Board object containing the current board
        Postconditions:
        - A string representation of the board is returned
        """
        representation = re.sub(r"[^\w-]", "", str(board))
        representation = re.sub(r"'", "", representation)
        return representation

    def load_board(self) -> list[list[str]]:
        """
        Loads the initial empty board.
        Postconditions:
        - The board is initialized with empty spaces ('-') in each cell.
        """
        # Loop through board
        for row in range(self.dim):
            for col in range(self.dim):
                self.board[row][col] = "-"
        return self.board

    def print_board(self) -> list[list[str]]:
        """
        Prints the current state of the game board.
        Postconditions:
        - The current state of the game board is printed to the console and de board is returned.
        """
        # Loop through board
        for row in range(self.dim):
            for col in range(self.dim):
                # Add grid of current board
                self.draw_grid(self.board[row][col])
            print()
            print()
        print()
        return self.board

    def draw_grid(self, letter: str) -> None:
        """
        Prints a single grid element with a letter.
        Precondition:
        - letter corresponds with a car and is a string.
        """
        # Print letter of corresponding car letter
        print(f"{str(letter).rjust(4)}", end="")

    def load_cars(self, filename: str) -> None:
        """
        Loads the car data from a CSV file.
        Preconditions:
        - filename is a string, the CSV file must exist and be properly formatted.
        """
        # Load data file
        with open(filename) as cars_data:
            next(cars_data)
            for line in cars_data:
                # Strip data when ','
                cars = line.strip().split(",")
                # Assign variable names with correct types
                car_name = cars[0]
                car_orientation = cars[1]
                car_col = int(cars[2]) - 1
                car_row = int(cars[3]) - 1
                car_len = int(cars[4])
                car = Car(car_name, car_orientation, car_col, car_row, car_len)
                self.cars[car_name] = car

    def add_cars(self, board: list[list[str]]) -> list[list[str]]:
        """
        Adds the cars to the game board.
        Preconditions:
        - board is a nested list with strings, but has no cars yet
        Postconditions:
        - The updated game board with the cars is returned.
        """
        # Loop through all cars in current gameboard
        for car_key in self.cars:
            # Find current car
            self.current_car = self.cars[car_key]
            # Find coordinates of current car
            list_coordinates = self.current_car.car_coordinates
            for coordinates in list_coordinates:
                # Find x and y coordinate
                y_coordinate = coordinates[0]
                x_coordinate = coordinates[1]
                board[y_coordinate][x_coordinate] = f"{car_key}"
        return board

    def random_car(self) -> str:
        """
        Returns a randomly selected car.
        Postconditions:
            - A string of a random carkey is selected and returned.
        """
        # Choice random carkey from all cars in current gameboard
        random_car = random.choice(list(self.cars.keys()))
        return random_car

    def get_possible_moves(self, board: "Board", car_key: str) -> tuple[list["Board"], bool]:
        """
        Determines the possible moves for a given car.
        Precondition:
        - board is a Board object representing the current board
        - car_key is a string, representing a certain car
        Postconditions:
        - A list with the possible boards(Board objects) and a boolean, which is True
        if the car can move, is returned
        """
        board.current_car = board.cars[car_key]
        # Find coordinates of current car
        list_coordinates = board.current_car.car_coordinates
        # Make list to add boards
        copy_boards = []
        # Get first car coordinate
        y, x = list_coordinates[0]
        # Check orientation
        if board.current_car.car_orientation == "H":
            movement_list = [(0, self.current_car.car_len), (0, -1)]
        elif board.current_car.car_orientation == "V":
            movement_list = [(self.current_car.car_len, 0), (-1, 0)]
        else:
            print("Invalid orientation")
        
        for dy, dx in movement_list:
            # Assign new coordinates
            new_y = y + dy
            new_x = x + dx
            # Check if grid of new coordinates is empty and not out of bounds
            if new_y >= 0 and new_y < board.dim and new_x >= 0 and new_x < board.dim and board.board[new_y][new_x] == "-":
                possible_coordinate = (new_y, new_x) 
                # Make copy of board
                copy_board = copy.deepcopy(board)
                # Make movement in copied board
                copy_board.move(car_key, possible_coordinate)
                # Add copied board with movement cars to list
                copy_boards.append(copy_board)

        # If car cannot move, an empty list[] and False is returned
        if len(copy_boards) == 0:
            return copy_boards, False

        return copy_boards, True

    def move(self, car_key: str, new_car_coordinates: tuple[int, int]) -> list[list[str]]:
        """
        Moves a car to a new position on the game board.
        Preconditions:
            - car_key is a string, representing the current car
            - new_car_coordinates is a list of possible coordinates for the current car
        Postconditions:
            - The board were the car is moved is returned. 
        """
        self.current_car = self.cars[car_key]
        new_board: list[list[str]] = []

        # If car cannot move return empty list
        if len(new_car_coordinates) == 0:
            return new_board
        
        # Assign current car coordinates
        current_car_coordinates = self.current_car.car_coordinates

        # Check orientation
        if self.current_car.car_orientation == "H":
            # Assign old car coordinate x
            car_x_coordinate = int(current_car_coordinates[-1][1])
            # Assign new car coordinate x
            x_coordinate = new_car_coordinates[1]
            # Check if car needs to move to the left or right
            if x_coordinate > car_x_coordinate:
                direction = 1
                # Add new coordinates to end of car coordinates list
                current_car_coordinates.append(new_car_coordinates)
                # Remove old coordinates from top of list
                current_car_coordinates.pop(0)
            else:
                direction = -1
                # Add new coordinates at the top of car coordinates list
                current_car_coordinates.insert(0, new_car_coordinates)
                # Remove old coordinates at the end of the car coordinates list
                current_car_coordinates.pop()
        elif self.current_car.car_orientation == "V":
            # Assign old car coordinate y
            car_y_coordinate = int(current_car_coordinates[-1][0])
            # Assing new car coordinate y
            y_coordinate = new_car_coordinates[0]
            # Check if car needst to move up or down
            if y_coordinate > car_y_coordinate:
                direction = 1
                # Add new car coordiantes to end of car coordinates list
                current_car_coordinates.append(new_car_coordinates)
                # Remove old coordinates from top of list
                current_car_coordinates.pop(0)
            else:
                direction = -1
                # Add new coordinates at the top of the car coordinates list
                current_car_coordinates.insert(0, new_car_coordinates)
                # Remove old coordinates at the end of the car coordinates list
                current_car_coordinates.pop()

        self.current_car.car_coordinates = current_car_coordinates
        # Adding move to move set
        move_id = 1
        if self.last_move:
            move_id = int(self.last_move.split()[-1]) + 1
        move = f"{car_key} {direction} {move_id}"
        self.move_set.add(move)
        self.last_move = move
        
        # Load board with new car coordinates
        new_board = self.load_board()
        new_board = self.add_cars(new_board)

        return new_board

    def is_won(self) -> bool:
        """
        Checks if the red car (X) is in winning configuration.
        Postconditions:
            - Returns True if the game has been won, False otherwise.
        """
        # Check size of board
        if self.dim == 6:
            # Find coordinates of red car ('player')
            red_car_coordinates = self.cars["X"].car_coordinates
            # Find end coordinates of red car
            x_start = red_car_coordinates[1][1]
            # Check if grid on the right of the car are all '-'
            while x_start + 1 < self.dim:
                x_start += 1
                if self.board[2][x_start] != "-":
                    return False
        elif self.dim == 9:
            # Find coordinates of red car ('player')
            red_car_coordinates = self.cars["X"].car_coordinates
            # Find end coordinates of red car
            x_start = red_car_coordinates[1][1]
            # Check if grid on the right of the car are all '-'
            while x_start + 1 < self.dim:
                x_start += 1
                if self.board[4][x_start] != "-":
                    return False
        elif self.dim == 12:
            # Find end coordinates of red car
            red_car_coordinates = self.cars["X"].car_coordinates
            # Find end coordinates of red car
            x_start = red_car_coordinates[1][1]
            # Check if grid on the right of the car are all '-'
            while x_start + 1 < self.dim:
                x_start += 1
                if self.board[5][x_start] != "-":
                    return False
        return True

    def use_solution(self, board: "Board", solution: "Board") -> set[str]:
        """
        Uses a given solution to move the board into winning configuration.
        Preconditions:
        - board is a Board object
        - solution is a nested list with strings containing the movements to solve the board
        """
        board.set_boards = {board.get_representation_breadth(board)}
        counter = 0
        for move in solution:
            counter += 1
            # Get car key and direction from move
            car_key = move[0]
            direction = move[1]
            # Get car object from board.cars
            board.current_car = board.cars[car_key]
            # Assign current car coordinates
            current_car_coordinates = board.current_car.car_coordinates

            # Check car orientation
            if board.current_car.car_orientation == "H":
                # Check direction
                if int(direction) == 1:
                    # Move to the right
                    new_y_coordinate = int(current_car_coordinates[0][0])
                    new_x_coordinate = current_car_coordinates[-1][1] + 1
                    new_right_car_coordinate = (new_y_coordinate, new_x_coordinate)
                    new_left_car_coordinate = current_car_coordinates[1]
                    # Add new coordinate to list
                    current_car_coordinates.append(new_right_car_coordinate)
                    # Remove old coordineate from list
                    current_car_coordinates.pop(0)
                elif int(direction) == -1:
                    # Move to the left
                    new_y_coordinate = int(current_car_coordinates[0][0])
                    new_x_coordinate = current_car_coordinates[0][-1] - 1
                    new_left_car_coordinate = (new_y_coordinate, new_x_coordinate)
                    new_right_car_coordinate = current_car_coordinates[0]
                    # Add new coordinate to list
                    current_car_coordinates.insert(0, new_left_car_coordinate)
                    # Remove old coordinate from list
                    current_car_coordinates.pop()
            elif board.current_car.car_orientation == "V":
                # Check direction
                if int(direction) == -1:
                    # Move down
                    new_x_coordinate = int(current_car_coordinates[0][1])
                    new_y_coordinate = current_car_coordinates[0][0] - 1
                    new_left_car_coordinate = (new_y_coordinate, new_x_coordinate)
                    new_right_car_coordinate = current_car_coordinates[0]
                    # Add new coordinate to list
                    current_car_coordinates.insert(0, new_left_car_coordinate)
                    # Remove old coordinate from list
                    current_car_coordinates.pop()
                elif int(direction) == 1:
                    # Move up
                    new_x_coordinate = int(current_car_coordinates[0][1])
                    new_y_coordinate = current_car_coordinates[-1][0] + 1
                    new_right_car_coordinate = (new_y_coordinate, new_x_coordinate)
                    new_left_car_coordinate = current_car_coordinates[1]
                    # Add new coordinate to list
                    current_car_coordinates.append(new_right_car_coordinate)
                    # Remove old coordinate from list
                    current_car_coordinates.pop(0)
            # visualize_board(board.board, board.cars, save_path=f"code/visualization/board_images/board{counter}.png")
            # Load board with new car coordinates
            board.current_car.car_coordinates = current_car_coordinates
            board.load_board()
            board.add_cars(board.board)
            # Add to set
            board.set_boards.add(board.get_representation_breadth(board))

        return board.set_boards

    def output(self, solution: list[list[str]]) -> None:
        """
        Writes a solution for a board into a csv file.
        Preconditions:
        - solution is a nested list with strings containing the movements to solve the board
        """
        with open("output/output.csv", "w") as file:
            writer = csv.writer(file)
            field = ["car", "move"]

            writer.writerow(field)

            for move in solution:
                car_key = move[0]
                direction = move[1]
                writer.writerow([car_key, direction])

    def order_strings_by_id(self) -> list[str]:
        """
        Orders the strings in move_set by their IDs.
        Postconditions:
        - Returns a list of strings from move_set, ordered by their IDs.
        """
        ordered_strings = sorted(self.move_set, key=lambda s: int(s.split(" ")[-1]))
        return ordered_strings

    def make_solution(self, ordered_solution: list[str]) -> list[list[str|int]]:
        """
        Creates a solution list from the ordered_solution list.
        Precondition:
        - ordered_solution is a list of strings in the format "<car> <direction> <id>".
        Postcondition:
        - Returns a nested list with strings, where each sublist contains the car and its corresponding direction as [car, direction].
        """
        for string in ordered_solution:
            car, direction, _ = string.split(" ")
            self.directions.append([car, int(direction)])
        return self.directions
    
    def order_solution(self) -> list[list[str|int]]:
        """
        Orders the solution based on the move_set.
        Postcondition:
        - Returns a list of lists, where each sublist contains the car and its corresponding direction as [car, direction].
        """
        ordered_solution = self.order_strings_by_id()
        solution = self.make_solution(ordered_solution)
        return solution
    
    def save_move_set(self, filename: str):
        """
        Saves the move set data to a file using pickle.
        Preconditions:
        - filename is a string representing the name of the file to save.
        """
        with open(filename, 'wb') as file:
            pickle.dump(self.move_set, file)

        print(f"Move set saved to {filename}.")

    def load_move_set(self, filename: str):
        """
        Loads the move set data from a file using pickle.
        Preconditions:
        - filename is a string representing the name of the file to load.
        """
        with open(filename, 'rb') as file:
            self.move_set = pickle.load(file)

        print(f"Move set loaded from {filename}.")