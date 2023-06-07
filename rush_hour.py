from cars import Car

class Rush_hour:
    def __init__(self, game) -> None:
        self.dim = int(game.strip().split("x")[0])
        self.board = [[i+j for j in range(self.dim)] for i in range(0, self.dim*self.dim, self.dim)]
        self.cars = {}

        self.load_board()
        self.print_board()
        
        self.load_cars(f"gameboards/Rushhour{game_name}.csv")
        print(self.cars)

    def load_board(self):
        
        counter = 1
        for col in range(self.dim):
            for row in range(self.dim):
                self.board[col][row] = counter
                counter += 1

        return self.board
    
    def print_board(self):
        for col in range(self.dim):
            for row in range(self.dim):
                self.draw_grid(self.board[col][row])
            print()
            print()
        return self.board

    def draw_grid(self, number):
        print(f"{str(number).rjust(4)}", end="")

    def load_cars(self, filename):
        with open(filename) as cars_data:
            next(cars_data)
            for line in cars_data:
                cars = line.strip().split(",")
                car_name = cars[0]
                car_orientation = cars[1]
                car_col = int(cars[2])
                car_row = int(cars[3])
                car_len = int(cars[4])
                car = Car(car_name, car_orientation, car_col, car_row, car_len)
                self.cars[car_name] = car
                self.current_car = self.cars[car_name]
                print(self.current_car.car_coordinates)


if __name__ == "__main__":

    from sys import argv

    if len(argv) != 2:
        print("Usage: python rush_hour.py [game]")
        exit(1)

    game_name = argv[1]

    rushhour = Rush_hour(game_name)
