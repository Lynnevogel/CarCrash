from .cars import Car
from sys import argv
import random

class Rush_hour:
    def __init__(self, game_name: str) -> None:
        # Extract dimension from name
        self.dim: int = int(game_name.strip().split("x")[0])
        # Initialize board
        self.board: list[list[str]] = [[str(i+j) for j in range(self.dim)] for i in range(0, self.dim*self.dim, self.dim)]
        # Intialize cars dictionary
        self.cars: dict[str, Car] = {}

        self.load_board()
 
        # Load data
        self.load_cars(f"gameboards/Rushhour{game_name}.csv")
        self.current_car: Car = self.cars['X']

        self.add_cars()
        self.print_board()

    # Loop through board and add grid
    def load_board(self) -> list[list[str]]:
        for row in range(self.dim):
            for col in range(self.dim):
                self.board[row][col] = "-"
        return self.board

    def print_board(self) -> list[list[str]]:
        for row in range(self.dim):
            for col in range(self.dim):
                self.draw_grid(self.board[row][col])
            print()
            print()
        return self.board

    def draw_grid(self, number: str) -> None:
        print(f"{str(number).rjust(4)}", end="")

    # Load car data
    def load_cars(self, filename: str) -> None:
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

    # Add cars to grid
    def add_cars(self) -> list[list[str]]:
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
        random_car = random.choice(list(self.cars.keys()))
        return self.cars[random_car]

    def can_move(self, car: Car) -> list[tuple[int, int]]:
        self.current_car = car
        list_coordinates = self.current_car.car_coordinates
        possible_coordinates = []
        for car_position in list_coordinates:
            y, x = car_position
            # print(f"y: {y}, x: {x}")

            if self.current_car.car_orientation == "H":
                for dy, dx in [(0, 1), (0, -1)]:
                    new_y = y + dy
                    new_x = x + dx
                    if new_y >= 0 and new_y < self.dim and new_x >= 0 and new_x < self.dim and self.board[new_y][new_x] == "-":
                        possible_coordinate = (new_y, new_x)
                        possible_coordinates.append(possible_coordinate)
                        # print(f"possible coordinates: {possible_coordinates}")
            elif self.current_car.car_orientation == "V":
                for dy, dx in [(1, 0), (-1, 0)]:
                    new_y = y + dy
                    new_x = x + dx
                    if new_y >= 0 and new_y < self.dim and new_x >= 0 and new_x < self.dim and self.board[new_y][new_x] == "-":
                        possible_coordinate = (new_y, new_x)
                        possible_coordinates.append(possible_coordinate)
                        # print(f"possible coordinates: {possible_coordinates}")
            else:
                print("Invalid orientation")
        return possible_coordinates

    def move(self, car: Car, possible_coordinates: list[tuple[int, int]]) -> bool:
        self.current_car = car
        # Position car needs to move to
        if len(possible_coordinates) == 0:
            print("Cannot move car :/")
            return False
        elif len(possible_coordinates) == 1:
            new_car_coordinates = possible_coordinates[0]
            print(f"new car coordinates: {new_car_coordinates}")
        elif len(possible_coordinates) == 2:
            new_car_coordinates = random.choice(possible_coordinates)
            print(f"new car coordinates 2: {new_car_coordinates}")

        # new_car_coordinates = (new_y, new_x)
        # Current car coordinates
        old_car_coordinates = self.current_car.car_coordinates
        if self.current_car.car_orientation == "H":
            # Biggest car coordinate on x-axis
            car_x_coordinate = int(old_car_coordinates[1][1])
            # Car needs to move on x-axis to this coordinate 
            x_coordinate = new_car_coordinates[1]

            if x_coordinate > car_x_coordinate:
                # add coordinates to back of list
                old_car_coordinates.append(new_car_coordinates)
                # remove coordinates from top of list
                old_car_coordinates.pop(0)
            else:
                # add coordinates to top of list
                old_car_coordinates.insert(0, new_car_coordinates)
                # remove coordinates from back of list
                old_car_coordinates.pop()

        elif self.current_car.car_orientation == "V":
            car_y_coordinate = int(old_car_coordinates[1][0])
            y_coordinate = new_car_coordinates[0]
            if y_coordinate > car_y_coordinate:
                # add coordinates to back of list
                old_car_coordinates.append(new_car_coordinates)
                # remove coordinates from list top of list
                old_car_coordinates.pop(0)
            else:
                # add coordinates to top of list
                old_car_coordinates.insert(0, new_car_coordinates)
                # remove coordinates from back of list
                old_car_coordinates.pop()

        self.current_car.car_coordinates = old_car_coordinates
        self.load_board()
        self.add_cars()
        return True

    def is_won(self) -> bool:
        """
        Checks if car X is in the winning configuration.
        pre: board is a 2D-list of size dim * dim
        post: returns True if the board is in the winning position
        (otherwise False)
        """
        if self.dim == 6:
            red_car_coordinates = self.cars["X"].car_coordinates
            x_start = red_car_coordinates[1][1]
            while x_start + 1 < self.dim:
                # print(x_start)
                x_start += 1
                if self.board[2][x_start] != "-":
                    return False
            print("You won!!")
        elif self.dim == 9:
            red_car_coordinates = self.cars["X"].car_coordinates
            x_start = red_car_coordinates[1][1]
            while x_start + 1 < self.dim:
                # print(x_start)
                x_start += 1
                if self.board[4][x_start] != "-":
                    return False
            print("You won!!")
        elif self.dim == 12:
            red_car_coordinates = self.cars["X"].car_coordinates
            x_start = red_car_coordinates[1][1]
            while x_start + 1 < self.dim:
                # print(x_start)
                x_start += 1
                if self.board[5][x_start] != "-":
                    return False
            print("You won!!")
        return True
