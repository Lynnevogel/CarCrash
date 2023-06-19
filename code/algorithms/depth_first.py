import copy


class DepthFirst:
    """
    A Depth First algorithm...
    """
    def __init__(self, board) -> None:
        self.board = copy.deepcopy(board)
        self.states = [copy.deepcopy(self.board)]
        self.existing_boards = [self.board.board]

    def get_next_state(self):
        return self.states.pop()

    def get_all_possible_states(self, moves, can_move):
        if can_move:
            for move in moves:
                if move.board not in self.existing_boards:
                    self.states.append(move)
                    self.existing_boards.append(move.board)

    def go(self):
        depth = 0
        while self.states:
            new_board = self.get_next_state()
            depth += 1 
            # print(f"new board: {new_board}")

            if new_board.is_won():
                print("WON")
                break
            else:
                for car in new_board.cars:
                    child = copy.deepcopy(new_board)
                    moves, can_move = child.get_possible_moves_2(child, car)
                    self.get_all_possible_states(moves, can_move)
            # print(f"states: {self.states}")
            print(f"states: {len(self.states)}")
        print(f"depth: {depth}")
