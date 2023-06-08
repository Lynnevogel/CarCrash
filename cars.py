class Car:
    def __init__(self, car_name, car_orientation, car_col, car_row, car_len) -> None:
        self.car_name = car_name
        self.car_orientation = car_orientation
        self.car_col = car_col
        self.car_row = car_row
        self.car_len = car_len
        self.car_coordinates = []
        self.car_placement()

    def __repr__(self) -> str:
        return f"{self.car_name} + {self.car_orientation} + {self.car_col} + {self.car_row} + {self.car_len} + {self.car_coordinates}"

    def car_placement(self):
        self.car_start_coordinate = (self.car_row, self.car_col)
        self.car_coordinates.append(self.car_start_coordinate)

        if self.car_len == 2:
            if self.car_orientation == "H":
                self.car_end_coordinate = (self.car_row, self.car_col + 1)
            else:
                self.car_end_coordinate = (self.car_row + 1, self.car_row)
            self.car_coordinates.append(self.car_end_coordinate)
        elif self.car_len == 3:
            if self.car_orientation == "H":
                self.car_middle_coordinate = (self.car_row, self.car_col + 1)
                self.car_end_coordinate = (self.car_row, self.car_col + 2)
            else:
                self.car_middle_coordinate = (self.car_row + 1, self.car_col)
                self.car_end_coordinate = (self.car_row + 2, self.car_col)
            self.car_coordinates.append(self.car_middle_coordinate)
            self.car_coordinates.append(self.car_end_coordinate)
        else:
            print("Invalid car length")

