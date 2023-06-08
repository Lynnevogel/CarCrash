from cars import Car
from sys import argv
import random

class Rush_hour:
    def __init__(self, game) -> None:
        # Extract dimension from name
        self.dim = int(game.strip().split("x")[0])
        # Initialize board
        self.board = [[i+j for j in range(self.dim)] for i in range(0, self.dim*self.dim, self.dim)]
        # Intialize cars dictionary
        self.cars = {}

        self.load_board()

        # Load data
        self.load_cars(f"gameboards/Rushhour{game_name}.csv")
        self.current_car = self.cars['X']

        self.add_cars()
        self.print_board()

    # Loop through board and add grid
    def load_board(self):
        for row in range(self.dim):
            for col in range(self.dim):
                self.board[row][col] = "-"

        return self.board
    
    def print_board(self):
        for row in range(self.dim):
            for col in range(self.dim):
                self.draw_grid(self.board[row][col])
            print()
            print()
        return self.board

    def draw_grid(self, number):
        print(f"{str(number).rjust(4)}", end="")

    # Load car data
    def load_cars(self, filename):
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
    def add_cars(self):
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

    def random_car(self):
        random_car = random.choice(list(self.cars.keys()))
        return self.cars[random_car]

    def can_move(self, car):
        self.current_car = car
        list_coordinates = self.current_car.car_coordinates
        for car_position in list_coordinates:
            y, x = car_position
            # print(f"y: {x}, x: {y}")

            if self.current_car.car_orientation == "H":
                for dy, dx in [(1, 0), (-1, 0)]:
                    new_y = y + dy
                    new_x = x + dx
                    # print(f"new: ({new_y}, {new_x})")
                    if new_y >= 0 and new_y < self.dim and new_x >= 0 and new_x < self.dim and self.board[new_y][new_x] == "-":
                        return new_y, new_x
            elif self.current_car.car_orientation == "V":
                for dy, dx in [(0, 1), (0, -1)]:
                    new_y = y + dy
                    new_x = x + dx
                    # print(f"new: ({new_y}, {new_x})")
                    if new_y >= 0 and new_y < self.dim and new_x >= 0 and new_x < self.dim and self.board[new_y][new_x] == "-":
                        return new_y, new_x
            else:
                print("Invalid orientation")
                return False
        return False

    def move(self, car, new_x, new_y):
        # print(car)
        print(f"new x: {new_x}")
        print(f"new y: {new_y}")


if __name__ == "__main__":

    if len(argv) != 2:
        print("Usage: python rush_hour.py [game]")
        exit(1)

    game_name = argv[1]

    rushhour = Rush_hour(game_name)

    random_car = rushhour.random_car()
    print(random_car)
    if rushhour.can_move(random_car):
        new_y, new_x = rushhour.can_move(random_car)
        # print(f"new_y = {new_y}, new_x = {new_x}")
        print("can move car")
        rushhour.move(random_car, new_y, new_x)
    else:
        print("cannot move car :(")
