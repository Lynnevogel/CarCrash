from cars import Car

class Rush_hour:
    def __init__(self, game) -> None:
        # Extract dimension from name
        self.dim = int(game.strip().split("x")[0])
        # Initialize board
        self.board = [[i+j for j in range(self.dim)] for i in range(0, self.dim*self.dim, self.dim)]
        # Intialize cars dictionary
        self.cars = {}

        self.load_board()
        self.print_board()
        
        # Load data
        self.load_cars(f"gameboards/Rushhour{game_name}.csv")
        self.current_car = self.cars['X']
        print(self.current_car) 
        
        self.find_car_coordinates()
        self.print_board()

    # Loop through board and add grid
    def load_board(self):
        for row in range(self.dim):
            for col in range(self.dim):
                self.board[col][row] = "-"

        return self.board
    
    def print_board(self):
        for row in range(self.dim):
            for col in range(self.dim):
                self.draw_grid(self.board[col][row])
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

    def find_car_coordinates(self):
        for car_key in self.cars:
            self.current_car = self.cars[car_key]
            for coordinates in self.current_car.car_coordinates:
                x_coordinate = coordinates[0]
                y_coordinate = coordinates[1]
                # print(f"{x_coordinate}, {y_coordinate}")
                self.add_cars(x_coordinate, y_coordinate, car_key)

    # Add cars to grid
    def add_cars(self, x_coordinate, y_coordinate, car_key):
        
        for col in range(self.dim):
            for row in range(self.dim):
                if col is x_coordinate and row is y_coordinate:
                    self.board[col][row] = f"{car_key}"
                
        return self.board

if __name__ == "__main__":

    from sys import argv

    if len(argv) != 2:
        print("Usage: python rush_hour.py [game]")
        exit(1)

    game_name = argv[1]

    rushhour = Rush_hour(game_name)
