from .cars import Car
from sys import argv
import random

class Rush_hour:
    def __init__(self, game_name: str) -> None:
        """
        Initializes the Rush Hour game.
        Preconditions:
            - The game_name format must be 'NxN_M', where N and M are positive integers.
        """
        # Extract dimension from name
        self.dim: int = int(game_name.strip().split("x")[0])
        # Initialize board
        self.board: list[list[str]] = [[str(i+j) for j in range(self.dim)] for i in range(0, self.dim*self.dim, self.dim)]
        # Initialize cars dictionary
        self.cars: dict[str, Car] = {}

         # Load data
        self.load_cars(f"gameboards/Rushhour{game_name}.csv")
        self.current_car: Car = self.cars['X']
        
        # intialize first board
        self.load_board()
        self.add_cars()
        self.print_board()

    def load_board(self) -> list[list[str]]:
        """
        Loads the initial empty board.
        Postconditions:
            - The board is initialized with empty spaces ('-') in each cell.
        """
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
        print(f"{str(letter).rjust(4)}", end="")

    def load_cars(self, filename: str) -> None:
        """
        Loads the car data from a CSV file.
        Preconditions:
            - The CSV file must exist and be properly formatted.
        """
        with open(filename) as cars_data:
            next(cars_data)
            for line in cars_data:
                cars = line.strip().split(",")
                car_name = cars[0]
                car_orientation = cars[1]
                car_col = int(cars[2]) - 1
                car_row = int(cars[3]) - 1
                car_len = int(cars[4])
                car = Car(car_name, car_orientation, car_col, car_row, car_len)
                self.cars[car_name] = car

    def add_cars(self) -> list[list[str]]:
        """
        Adds the cars to the game board.
        Postconditions:
            - The cars are added to the game board.
            - The updated game board is returned.
        """
        for car_key in self.cars:
            self.current_car = self.cars[car_key]
            list_coordinates = self.current_car.car_coordinates
            for coordinates in list_coordinates:
                x_coordinate = coordinates[0]
                y_coordinate = coordinates[1]
                for row in range(self.dim):
                    for col in range(self.dim):
                        if row is x_coordinate and col is y_coordinate:
                            self.board[row][col] = f"{car_key}" 
        return self.board

    def random_car(self) -> Car:
        """
        Returns a randomly selected car.
        Postconditions:
            - A random car object is selected and returned.
        """
        random_car = random.choice(list(self.cars.keys()))
        return self.cars[random_car]

    def can_move(self, car: Car) -> list[tuple[int, int]]:
        """
        Determines the possible moves for a given car.
        Precondition:
            - car is a Car object.
        Postconditions:
            - The possible coordinates for the car are determined and returned in a list.
        """
        self.current_car = car
        list_coordinates = self.current_car.car_coordinates
        possible_coordinates = []
        for car_position in list_coordinates:
            y, x = car_position

            if self.current_car.car_orientation == "H":
                for dy, dx in [(0, 1), (0, -1)]:
                    new_y = y + dy
                    new_x = x + dx
                    if new_y >= 0 and new_y < self.dim and new_x >= 0 and new_x < self.dim and self.board[new_y][new_x] == "-":
                        possible_coordinate = (new_y, new_x)
                        possible_coordinates.append(possible_coordinate)
            elif self.current_car.car_orientation == "V":
                for dy, dx in [(1, 0), (-1, 0)]:
                    new_y = y + dy
                    new_x = x + dx
                    if new_y >= 0 and new_y < self.dim and new_x >= 0 and new_x < self.dim and self.board[new_y][new_x] == "-":
                        possible_coordinate = (new_y, new_x)
                        possible_coordinates.append(possible_coordinate)
            else:
                print("Invalid orientation")
        return possible_coordinates

    def move(self, car: Car, possible_coordinates: list[tuple[int, int]]) -> bool:
        """
        Moves a car to a new position on the game board.
        Preconditions:
            - car is a Car object.
            - The 'possible_coordinates' is a list of possible coordinates for the variable car.
        Postconditions:
            - The car is moved to the new position on the game board.
            - Returns True if the car is successfully moved, False otherwise.
        """
        self.current_car = car

        if len(possible_coordinates) == 0:
            print("Cannot move car.")
            return False
        elif len(possible_coordinates) == 1:
            new_car_coordinates = possible_coordinates[0]
        elif len(possible_coordinates) == 2:
            new_car_coordinates = random.choice(possible_coordinates)

        old_car_coordinates = self.current_car.car_coordinates

        if self.current_car.car_orientation == "H":
            car_x_coordinate = int(old_car_coordinates[1][1])
            x_coordinate = new_car_coordinates[1]

            if x_coordinate > car_x_coordinate:
                old_car_coordinates.append(new_car_coordinates)
                old_car_coordinates.pop(0)
            else:
                old_car_coordinates.insert(0, new_car_coordinates)
                old_car_coordinates.pop()
        elif self.current_car.car_orientation == "V":
            car_y_coordinate = int(old_car_coordinates[1][0])
            y_coordinate = new_car_coordinates[0]

            if y_coordinate > car_y_coordinate:
                old_car_coordinates.append(new_car_coordinates)
                old_car_coordinates.pop(0)
            else:
                old_car_coordinates.insert(0, new_car_coordinates)
                old_car_coordinates.pop()

        self.current_car.car_coordinates = old_car_coordinates
        self.load_board()
        self.add_cars()
        return True

    def is_won(self) -> bool:
        """
        Checks if the red car (X) is in winning configuration.
        Postconditions:
            - Returns True if the game has been won, False otherwise.
        """
        if self.dim == 6:
            red_car_coordinates = self.cars["X"].car_coordinates
            x_start = red_car_coordinates[1][1]
            while x_start + 1 < self.dim:
                x_start += 1
                if self.board[2][x_start] != "-":
                    return False
        elif self.dim == 9:
            red_car_coordinates = self.cars["X"].car_coordinates
            x_start = red_car_coordinates[1][1]
            while x_start + 1 < self.dim:
                x_start += 1
                if self.board[4][x_start] != "-":
                    return False
        elif self.dim == 12:
            red_car_coordinates = self.cars["X"].car_coordinates
            x_start = red_car_coordinates[1][1]
            while x_start + 1 < self.dim:
                x_start += 1
                if self.board[5][x_start] != "-":
                    return False
        return True
