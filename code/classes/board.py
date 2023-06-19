from .cars import Car
import random
import copy
from typing import Any


class Board:
    def __init__(self, game_name: str) -> None:
        """
        Initializes the Rush Hour game.
        Preconditions:
            - The game_name format must be 'NxN_M', where N and M are positive integers.
        """
        # Extract dimension from name
        self.dim: int = int(game_name.strip().split("x")[0])
        # Initialize board
        self.board = [["-" for _ in range(self.dim)] for _ in range(self.dim)]
        self.cars: dict[str, Car] = {}

         # Load data
        self.load_cars(f"gameboards/Rushhour{game_name}.csv")
        self.current_car: Car = self.cars['X']
        
        # Intialize first board
        self.load_board()
        self.add_cars(self.board)
        self.print_board()

    def __repr__(self) -> str:
        return f"{self.print_board()}"

    def load_board(self) -> list[list[str]]:
        """
        Loads the initial empty board.
        Postconditions:
            - The board is initialized with empty spaces ('-') in each cell.
        """
        # Loop through board and initialize with '-'
        for row in range(self.dim):
            for col in range(self.dim):
                self.board[row][col] = "-"
        return self.board

    def print_board(self) -> list[list[str]]:
        """
        Prints the current state of the game board.
        Postconditions:
            - The current state of the game board is printed to the console.
        """
        # Loop through board and print corresponding grids
        for row in range(self.dim):
            for col in range(self.dim):
                self.draw_grid(self.board[row][col])
            print()
            print()
        print()
        return self.board

    def draw_grid(self, letter: str) -> None:
        """
        Prints a single grid element with a letter.
        Precondition:
            - Letter corresponds with a car and is a string.
        """
        # Print letter of corresponding car
        print(f"{str(letter).rjust(4)}", end="")

    def load_cars(self, filename: str) -> None:
        """
        Loads the car data from a CSV file.
        Preconditions:
            - The CSV file must exist and be properly formatted.
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
            - The board were the cars need to be added
        Postconditions:
            - The cars are added to the game board.
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
                x_coordinate = coordinates[0]
                y_coordinate = coordinates[1]
                # Loop through board
                for row in range(self.dim):
                    for col in range(self.dim):
                        # Find car coordinates in board
                        if row is x_coordinate and col is y_coordinate:
                            # Add car_key to coordinate
                            board[row][col] = f"{car_key}"
        return board

    def random_car(self) -> str:
        """
        Returns a randomly selected car.
        Postconditions:
            - A random carkey is selected and returned.
        """
        # Choice random carkey from all cars in current gameboard
        random_car = random.choice(list(self.cars.keys()))
        return random_car

    def get_possible_moves(self, car_key: str) -> tuple[list[Any], bool]:
        """
        Determines the possible moves for a given car.
        Precondition:
            - car_key is a string
        Postconditions:
            - The possible coordinates for the car are determined and returned in a list.
        """
        self.current_car = self.cars[car_key]
        # Find coordinates of current car
        list_coordinates = self.current_car.car_coordinates
        # Make list to add boards
        copy_boards = []
        # Loop through car coordinates of current car
        for car_position in list_coordinates:
            y, x = car_position

            # Check orientation
            if self.current_car.car_orientation == "H":
                # Loop through horizontal grid 
                for dy, dx in [(0, 1), (0, -1)]:
                    # Assign new coordinates
                    new_y = y + dy
                    new_x = x + dx
                    # Check if grid of new coordinates is empty and not out of bounds
                    if new_y >= 0 and new_y < self.dim and new_x >= 0 and new_x < self.dim and self.board[new_y][new_x] == "-":
                        possible_coordinate = (new_y, new_x) 
                        # Make copy of board
                        copy_board = copy.deepcopy(self)
                        # Make movement in copied board
                        copy_board.move(car_key, possible_coordinate)
                        # Add copied board with movement cars to list
                        copy_boards.append(copy_board)
            elif self.current_car.car_orientation == "V":
                # Loop through vertical grid
                for dy, dx in [(1, 0), (-1, 0)]:
                    # Assign new coordinates
                    new_y = y + dy
                    new_x = x + dx
                    # Check if grid of new coordinates is empty and not out of bounds
                    if new_y >= 0 and new_y < self.dim and new_x >= 0 and new_x < self.dim and self.board[new_y][new_x] == "-":
                        possible_coordinate = (new_y, new_x)
                        # Make copy of board
                        copy_board = copy.deepcopy(self)
                        # Make movement in copied board
                        copy_board.move(car_key, possible_coordinate)
                        # Add copied board with movement cars to list
                        copy_boards.append(copy_board)

            else:
                print("Invalid orientation")

        # If car cannot move, an empty list and False wil be returned
        if len(copy_boards) == 0:
            return copy_boards, False

        return copy_boards, True
    
    def get_possible_moves_2(self, board, car_key: str) -> tuple[list[Any], bool]:
        """
        Determines the possible moves for a given car.
        Precondition:
            - car_key is a string
        Postconditions:
            - The possible coordinates for the car are determined and returned in a list.
        """
        self.current_car = self.cars[car_key]
        # Find coordinates of current car
        list_coordinates = self.current_car.car_coordinates
        # Make list to add boards
        copy_boards = []
        # Loop through car coordinates of current car
        for car_position in list_coordinates:
            y, x = car_position

            # Check orientation
            if self.current_car.car_orientation == "H":
                # Loop through horizontal grid 
                for dy, dx in [(0, 1), (0, -1)]:
                    # Assign new coordinates
                    new_y = y + dy
                    new_x = x + dx
                    # Check if grid of new coordinates is empty and not out of bounds
                    if new_y >= 0 and new_y < self.dim and new_x >= 0 and new_x < self.dim and self.board[new_y][new_x] == "-":
                        possible_coordinate = (new_y, new_x) 
                        # Make copy of board
                        copy_board = copy.deepcopy(board)
                        # Make movement in copied board
                        copy_board.move(car_key, possible_coordinate)
                        # Add copied board with movement cars to list
                        copy_boards.append(copy_board)
            elif self.current_car.car_orientation == "V":
                # Loop through vertical grid
                for dy, dx in [(1, 0), (-1, 0)]:
                    # Assign new coordinates
                    new_y = y + dy
                    new_x = x + dx
                    # Check if grid of new coordinates is empty and not out of bounds
                    if new_y >= 0 and new_y < self.dim and new_x >= 0 and new_x < self.dim and self.board[new_y][new_x] == "-":
                        possible_coordinate = (new_y, new_x)
                        # Make copy of board
                        copy_board = copy.deepcopy(self)
                        # Make movement in copied board
                        copy_board.move(car_key, possible_coordinate)
                        # Add copied board with movement cars to list
                        copy_boards.append(copy_board)

            else:
                print("Invalid orientation")

        # If car cannot move, an empty list and False wil be returned
        if len(copy_boards) == 0:
            return copy_boards, False

        return copy_boards, True

    def move(self, car_key: str, new_car_coordinates: tuple[int, int]) -> list[list[str]]:
        """
        Moves a car to a new position on the game board.
        Preconditions:
            - car is a Car object.
            - The 'new_car_coordinates' is a list of possible coordinates for the variable car.
        Postconditions:
            - The car is moved to the new position on the game board.
            - Returns True if the car is successfully moved, False otherwise.
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
            car_x_coordinate = int(current_car_coordinates[1][1])
            # Assign new car coordinate x
            x_coordinate = new_car_coordinates[1]
            # Check if car needs to move to the left or right
            if x_coordinate > car_x_coordinate:
                # Add new coordinates to end of car coordinates list
                current_car_coordinates.append(new_car_coordinates)
                # Remove old coordinates from top of list
                current_car_coordinates.pop(0)
            else:
                # Add new coordinates at the top of car coordinates list
                current_car_coordinates.insert(0, new_car_coordinates)
                # Remove old coordinates at the end of the car coordinates list
                current_car_coordinates.pop()
        elif self.current_car.car_orientation == "V":
            # Assign old car coordinate y
            car_y_coordinate = int(current_car_coordinates[1][0])
            # Assing new car coordinate y
            y_coordinate = new_car_coordinates[0]
            # Check if car needst to move up or down
            if y_coordinate > car_y_coordinate:
                # Add new car coordiantes to end of car coordinates list
                current_car_coordinates.append(new_car_coordinates)
                # Remove old coordinates from top of list
                current_car_coordinates.pop(0)
            else:
                # Add new coordinates at the top of the car coordinates list
                current_car_coordinates.insert(0, new_car_coordinates)
                # Remove old coordinates at the end of the car coordinates list
                current_car_coordinates.pop()

        self.current_car.car_coordinates = current_car_coordinates
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

    def track_moves(self, car_key: str, direction: str) -> None:
        print(f"car key: {car_key}")
        print(f"direction: {direction}")
