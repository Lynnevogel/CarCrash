class Car:
    def __init__(self, car_name: str, car_orientation: str, car_col: int, car_row: int, car_len: int) -> None:
        """
        Initializes a car object.
        Preconditions:
        - car_name is a string.
        - car_orientation is either "H" or "V".
        - car_col, car_row and car_len are positive integers.
        """
        # Get car information
        self.car_name: str = car_name
        self.car_orientation: str = car_orientation
        self.car_col: int = car_col
        self.car_row: int = car_row
        self.car_len: int = car_len
        self.car_coordinates: list[tuple[int, int]] = []
        self.car_placement()

    def __repr__(self) -> str:
        """
        Returns a string representation of the car object.
        Postconditions:
        - Returns a string representation of the car object.
        """
        return f"{self.car_name} + {self.car_orientation} + {self.car_len} + {self.car_coordinates}"

    def car_placement(self) -> None:
        """
        Determines the coordinates of the car based on its orientation and length.
        """
        # Add start coordinates to coordinates list
        self.car_start_coordinate = (self.car_row, self.car_col)
        self.car_coordinates.append(self.car_start_coordinate)

        # Check car lenght 
        if self.car_len == 2:
            # Check orientation
            if self.car_orientation == "H":
                # Find end car coordinates
                self.car_end_coordinate = (self.car_row, self.car_col + 1)
            else:
                # Find end car coordinates
                self.car_end_coordinate = (self.car_row + 1, self.car_col)
            # Append end coordinates to coordinates list
            self.car_coordinates.append(self.car_end_coordinate)
        elif self.car_len == 3:
            # Check orientation
            if self.car_orientation == "H":
                # Find middle and end car coordinates
                self.car_middle_coordinate = (self.car_row, self.car_col + 1)
                self.car_end_coordinate = (self.car_row, self.car_col + 2)
            else:
                # Find middle and end car coordinates
                self.car_middle_coordinate = (self.car_row + 1, self.car_col)
                self.car_end_coordinate = (self.car_row + 2, self.car_col)
            # Append middle and end coordinates to coordinates list
            self.car_coordinates.append(self.car_middle_coordinate)
            self.car_coordinates.append(self.car_end_coordinate)
        else:
            print("Invalid car length")
