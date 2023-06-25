import copy
from code.algorithms.depth_first import DepthFirst
from code.classes.board import Board
from typing import Optional, Any


class IterativeDeepening:
    """
    Iterative deepening...
    """

    def __init__(self, board: Board, maxDepth) -> None:
        self.board = copy.deepcopy(board)

        self.states = [copy.deepcopy(self.board)]
        self.archive = {self.board.get_representation(self.board)}
        self.number_of_moves = []
        self.maxDepth = maxDepth
        self.won = 0 

        self.newstack = []

    
        self.best_solution = []
        self.best_value = float('inf')


    def get_next_state(self) -> Board:
        """
        Returns the last added state from the states list.
        """
        return self.states.pop()
    
    def add_all_possible_states(self, can_move: bool, moves: list[Any]) -> None:
        """
        Adds states to the states list and keeps an archive of states that should not be 
        added to the states list.
        """
        
        if can_move:
            for move in moves:
                if move.get_representation(move) not in self.archive and len(move.directions) < 200:
                    self.states.append(move)

    def check_solution(self, new_board: Optional[Board]) -> None:
        """
        Checks whether the solution contains fewer moves than the current best solution.
        """
        move_count = len(new_board.directions)
        print(f"move count: {move_count}")

        if self.number_of_moves:
                lowest_value = min(self.number_of_moves)
                if move_count < lowest_value:
                    self.number_of_moves.append(move_count)
                    self.best_solution = []
                    self.best_solution.append(new_board.directions)
        elif move_count > 0:
            self.number_of_moves.append(move_count)

        print(f"number of moves: {move_count}")

    def iterativeDeepening(self) -> None:
        """
        Applies the iterative deepening algorithm to the depth-first search.
        """
        # for i in range(self.maxDepth + 1):
        #     print(f"Max i: {i}")
        #     if self.DFS(self.board, i):
        #         return True
        # return False

        maxDepth = 0
        while True:  # Set maximum depth to 100
            print(f"Max Depth: {maxDepth}")
            if self.DFS(self.board, maxDepth):
                return 
            maxDepth += 1

        return

    def DFS(self, new_board: Board, Maxdepth: int) -> bool:
        """
        Performs a depth-limited search (DFS) with the given depth.
        """
        if Maxdepth == 0:
            return False
        print(len(self.states))
        while self.states and len(new_board.directions) < Maxdepth:
            new_board = self.get_next_state()
            print(f"new_board{new_board}")
            new_board_representation = new_board.get_representation(new_board)
            self.archive.add(new_board_representation)
            # print(f"states: {len(self.states)}")
            if new_board.is_won():
                print("WON")
                # self.won = 1
                # remove winning state from archive
                self.archive.remove(new_board_representation)
                # check whether solution is better than current best solution
                self.check_solution(new_board)
                return True
            else:
                for car in new_board.cars:
                    child = copy.deepcopy(new_board)
                    # get possible board states from current car
                    moves, can_move = child.get_possible_moves(child, car)
                    print(f"moves: {moves}")
                    print(f"canmove: {can_move}")

                    # add possible board states to list of states
                    self.add_all_possible_states(new_board, can_move, moves)
                    print(f"depht: {len(new_board.directions)}")
                    print(f"i: {Maxdepth}")
                    if len(new_board.directions) < Maxdepth:
                        return False
            
        if len(new_board.directions) == Maxdepth - 1:
            # new_board = self.get_next_state()
            self.DFS(new_board, Maxdepth)
                

        if len(self.states) == 0:
            exit(1)
                    
            #return False

    def go(self) -> None:
        """
        Runs the iterative deepening depth-first search algorithm until all possible states have been visited.
        """
        self.iterativeDeepening()
        
        # Print the best solution and the number of moves
        # print(f"lowest amount of moves: {self.number_of_moves[-1]}")
        print(f"moves of best solution: {self.best_solution}")
